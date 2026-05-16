"""Classical lagged-edge scoring baselines for synthetic recovery."""

from __future__ import annotations

import numpy as np


def _zscore(x: np.ndarray) -> np.ndarray:
    return (x - x.mean(axis=0, keepdims=True)) / (x.std(axis=0, keepdims=True) + 1e-8)


def make_lagged_design(x: np.ndarray, max_lag: int) -> tuple[np.ndarray, np.ndarray]:
    """Build a lag-major design matrix for VAR-style regression."""

    if x.ndim != 2:
        raise ValueError(f"Expected x with shape (timesteps, n_nodes), got {x.shape}")
    timesteps, _ = x.shape
    if timesteps <= max_lag + 1:
        raise ValueError("Need more timesteps than max_lag + 1")

    features = []
    for lag in range(1, max_lag + 1):
        features.append(x[max_lag - lag : timesteps - lag])
    design = np.concatenate(features, axis=1)
    target = x[max_lag:]
    return design, target


def random_scores(n_nodes: int, max_lag: int, seed: int = 0) -> np.ndarray:
    """Random non-self lagged edge scores for a chance baseline."""

    rng = np.random.default_rng(seed)
    scores = rng.random((max_lag, n_nodes, n_nodes))
    for node in range(n_nodes):
        scores[:, node, node] = 0.0
    return scores


def ridge_var_scores(x: np.ndarray, max_lag: int, alpha: float = 1.0) -> np.ndarray:
    """Fit a ridge VAR and use absolute coefficients as lagged edge scores."""

    scores = np.abs(ridge_var_coefficients(x, max_lag=max_lag, alpha=alpha))
    for node in range(scores.shape[1]):
        scores[:, node, node] = 0.0
    return scores


def ridge_var_coefficients(x: np.ndarray, max_lag: int, alpha: float = 1.0) -> np.ndarray:
    """Fit a ridge VAR and return signed lagged coefficients."""

    _, n_nodes = x.shape
    design, target = make_lagged_design(_zscore(x), max_lag)
    design = _zscore(design)
    target = _zscore(target)

    gram = design.T @ design
    penalty = alpha * np.eye(gram.shape[0])
    coeff = np.linalg.solve(gram + penalty, design.T @ target)
    scores = coeff.reshape(max_lag, n_nodes, n_nodes)
    for node in range(n_nodes):
        scores[:, node, node] = 0.0
    return scores


def lasso_var_scores(x: np.ndarray, max_lag: int, alpha: float = 0.005) -> np.ndarray:
    """Fit one Lasso regression per target and score absolute coefficients."""

    from sklearn.linear_model import Lasso

    _, n_nodes = x.shape
    design, target = make_lagged_design(_zscore(x), max_lag)
    design = _zscore(design)
    target = _zscore(target)

    coeff = np.zeros((max_lag * n_nodes, n_nodes), dtype=float)
    for target_idx in range(n_nodes):
        model = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000, selection="cyclic")
        model.fit(design, target[:, target_idx])
        coeff[:, target_idx] = model.coef_

    scores = np.abs(coeff.reshape(max_lag, n_nodes, n_nodes))
    for node in range(n_nodes):
        scores[:, node, node] = 0.0
    return scores


def _ols_rss(design: np.ndarray, target: np.ndarray) -> float:
    coefficients, *_ = np.linalg.lstsq(design, target, rcond=None)
    residual = target - design @ coefficients
    return float(residual.T @ residual)


def granger_f_scores(x: np.ndarray, max_lag: int) -> np.ndarray:
    """Score lagged edges with conditional Granger-style F statistics.

    Each score compares the full lagged linear model for a target node against
    a restricted model that removes one source-lag feature while conditioning
    on every other lagged source. This provides a classical hypothesis-test
    family beside coefficient-magnitude VAR baselines.
    """

    _, n_nodes = x.shape
    design, target = make_lagged_design(_zscore(x), max_lag)
    design = _zscore(design)
    target = _zscore(target)
    n_rows, n_features = design.shape
    df_den = max(1, n_rows - n_features)
    scores = np.zeros((max_lag, n_nodes, n_nodes), dtype=float)

    for target_idx in range(n_nodes):
        y = target[:, target_idx]
        full_rss = max(_ols_rss(design, y), 1e-12)
        full_mse = full_rss / float(df_den)
        for lag in range(max_lag):
            for source_idx in range(n_nodes):
                if source_idx == target_idx:
                    continue
                feature_idx = lag * n_nodes + source_idx
                restricted = np.delete(design, feature_idx, axis=1)
                restricted_rss = _ols_rss(restricted, y)
                numerator = max(0.0, restricted_rss - full_rss)
                scores[lag, source_idx, target_idx] = numerator / full_mse
    return scores


def pcmci_parcorr_scores(
    x: np.ndarray,
    max_lag: int,
    pc_alpha: float = 0.05,
    score: str = "statistic",
) -> np.ndarray:
    """Score lagged edges with Tigramite PCMCI using ParCorr tests.

    Tigramite returns matrices indexed as ``source, target, tau``. This
    function converts them to the repository convention
    ``lag, source, target`` so that recovery metrics and downstream graph
    utilities can consume PCMCI scores without special handling.
    """

    try:
        from tigramite import data_processing as pp
        from tigramite.independence_tests.parcorr import ParCorr
        from tigramite.pcmci import PCMCI
    except ImportError as exc:
        raise ImportError(
            "PCMCI-ParCorr requires tigramite; install it with "
            "`python -m pip install tigramite`."
        ) from exc

    if score not in {"statistic", "p_value"}:
        raise ValueError("score must be 'statistic' or 'p_value'")

    dataframe = pp.DataFrame(_zscore(x))
    pcmci = PCMCI(
        dataframe=dataframe,
        cond_ind_test=ParCorr(significance="analytic"),
        verbosity=0,
    )
    results = pcmci.run_pcmci(tau_min=1, tau_max=max_lag, pc_alpha=pc_alpha)

    if score == "statistic":
        source_target_lag = np.abs(results["val_matrix"][:, :, 1 : max_lag + 1])
    else:
        p_values = np.clip(results["p_matrix"][:, :, 1 : max_lag + 1], 1e-300, 1.0)
        source_target_lag = -np.log10(p_values)

    scores = np.moveaxis(source_target_lag, 2, 0)
    scores = np.nan_to_num(scores, nan=0.0, posinf=300.0, neginf=0.0)
    for node in range(scores.shape[1]):
        scores[:, node, node] = 0.0
    return scores


def sliding_window_bounds(
    timesteps: int,
    max_lag: int,
    window_size: int | None = None,
    stride: int | None = None,
) -> list[tuple[int, int]]:
    """Return deterministic sliding-window bounds for local temporal scoring."""

    min_window = max(4 * max_lag + 20, max_lag + 2)
    if window_size is None:
        window_size = max(min_window, min(timesteps // 2, 300))
    if stride is None:
        stride = max(1, window_size // 2)
    if window_size <= max_lag + 1:
        raise ValueError("window_size must be greater than max_lag + 1")
    if stride <= 0:
        raise ValueError("stride must be positive")
    if timesteps < window_size:
        return [(0, timesteps)]

    bounds: list[tuple[int, int]] = []
    start = 0
    while start + window_size <= timesteps:
        bounds.append((start, start + window_size))
        start += stride

    final = (timesteps - window_size, timesteps)
    if bounds[-1] != final:
        bounds.append(final)
    return bounds


def _aggregate_window_scores(window_scores: list[np.ndarray], aggregate: str) -> np.ndarray:
    stacked = np.stack(window_scores, axis=0)
    if aggregate == "max":
        return stacked.max(axis=0)
    if aggregate == "mean":
        return stacked.mean(axis=0)
    if aggregate == "p90":
        return np.quantile(stacked, 0.90, axis=0)
    raise ValueError(f"Unknown aggregate mode: {aggregate}")


def dynamic_ridge_var_scores(
    x: np.ndarray,
    max_lag: int,
    alpha: float = 1.0,
    window_size: int | None = None,
    stride: int | None = None,
    aggregate: str = "max",
) -> np.ndarray:
    """Score edges by aggregating local ridge VAR fits over sliding windows."""

    timesteps, _ = x.shape
    scores = [
        ridge_var_scores(x[start:end], max_lag=max_lag, alpha=alpha)
        for start, end in sliding_window_bounds(timesteps, max_lag, window_size, stride)
    ]
    return _aggregate_window_scores(scores, aggregate)


def dynamic_lasso_var_scores(
    x: np.ndarray,
    max_lag: int,
    alpha: float = 0.005,
    window_size: int | None = None,
    stride: int | None = None,
    aggregate: str = "max",
) -> np.ndarray:
    """Score edges by aggregating local Lasso VAR fits over sliding windows."""

    timesteps, _ = x.shape
    scores = [
        lasso_var_scores(x[start:end], max_lag=max_lag, alpha=alpha)
        for start, end in sliding_window_bounds(timesteps, max_lag, window_size, stride)
    ]
    return _aggregate_window_scores(scores, aggregate)


def dynamic_granger_f_scores(
    x: np.ndarray,
    max_lag: int,
    window_size: int | None = None,
    stride: int | None = None,
    aggregate: str = "max",
) -> np.ndarray:
    """Score edges by aggregating local Granger F-tests over sliding windows."""

    timesteps, _ = x.shape
    scores = [
        granger_f_scores(x[start:end], max_lag=max_lag)
        for start, end in sliding_window_bounds(timesteps, max_lag, window_size, stride)
    ]
    return _aggregate_window_scores(scores, aggregate)
