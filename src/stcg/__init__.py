"""Utilities for temporal graph structure discovery experiments."""

from .baselines import dynamic_granger_f_scores, dynamic_lasso_var_scores, dynamic_ridge_var_scores
from .baselines import granger_f_scores, lasso_var_scores, pcmci_parcorr_scores
from .baselines import random_scores, ridge_var_coefficients, ridge_var_scores, sliding_window_bounds
from .forecasting import ForecastSplit, chronological_lagged_split, forecast_metrics
from .forecasting import graph_feature_mask, graph_feature_weights
from .forecasting import persistence_forecast, ridge_forecast, ridge_forecast_weighted
from .metrics import edge_auc, lagged_correlation_scores, precision_at_k, recovery_summary
from .metrics import lag_recovery_accuracy, pair_edge_auc, structural_hamming_distance
from .self_supervised import STCGConfig, STCGStateConfig, STCGStateDiagnostics
from .self_supervised import stcg_v0_scores, stcg_v1_diagnostics, stcg_v1_scores
from .synthetic import SyntheticDataset, generate_lagged_var

__all__ = [
    "STCGConfig",
    "STCGStateConfig",
    "STCGStateDiagnostics",
    "SyntheticDataset",
    "ForecastSplit",
    "chronological_lagged_split",
    "edge_auc",
    "forecast_metrics",
    "generate_lagged_var",
    "granger_f_scores",
    "graph_feature_mask",
    "graph_feature_weights",
    "lag_recovery_accuracy",
    "lagged_correlation_scores",
    "lasso_var_scores",
    "dynamic_granger_f_scores",
    "dynamic_lasso_var_scores",
    "dynamic_ridge_var_scores",
    "pair_edge_auc",
    "pcmci_parcorr_scores",
    "precision_at_k",
    "persistence_forecast",
    "random_scores",
    "recovery_summary",
    "ridge_var_coefficients",
    "ridge_forecast",
    "ridge_forecast_weighted",
    "ridge_var_scores",
    "sliding_window_bounds",
    "stcg_v0_scores",
    "stcg_v1_diagnostics",
    "stcg_v1_scores",
    "structural_hamming_distance",
]
