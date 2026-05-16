# Real Data Ingestion Checklist

Last updated: 2026-05-14 Asia/Shanghai.

This checklist defines the minimum requirements for adding a real multivariate time-series CSV to the STCG downstream benchmark path.

## Required CSV Shape

- Place the file under `data/raw/`.
- Use one row per timestamp.
- Include at least two numeric signal columns.
- Include a timestamp column if available.
- Keep rows in chronological order, or sort them before running the benchmark.
- Avoid duplicate timestamps unless they have already been aggregated.

Recommended layout:

```text
timestamp,node_a,node_b,node_c,node_d
2024-01-01 00:00:00,1.0,0.4,2.1,7.0
2024-01-01 01:00:00,1.1,0.5,2.0,6.8
```

## Minimum Data Checks

Before running:

- At least 300 rows for an initial smoke test.
- Prefer 1000+ rows for dynamic graph-state evaluation.
- At least 4 numeric columns if graph interpretation is expected.
- Missing values should be sparse enough for interpolation or row dropping.
- Remove ID columns, categorical columns, and target labels unless they are intended as numeric signals.
- Do not include future-derived or leakage-prone columns.

## Default Command

First inspect local CSV availability and basic schema:

```powershell
python scripts\fetch_ett_benchmarks.py
python scripts\check_real_data_inventory.py
```

The inventory step writes `results/tables/real_data_inventory.csv` and `results/tables/real_data_inventory.md`.

Then create a dry-run execution plan for every `ready` or `warning` CSV:

```powershell
python scripts\run_real_benchmark_from_inventory.py
```

The plan step writes `results/tables/real_benchmark_run_plan.md`.
Add `--execute` only when the listed commands and output locations look correct.
After execution, summarize the per-dataset outputs:

```powershell
python scripts\summarize_real_benchmarks.py
```

```powershell
python scripts\run_downstream_forecasting.py --input-csv data\raw\<dataset>.csv --time-column <timestamp_column> --dataset-name <dataset_name>
```

If only selected signal columns should be used:

```powershell
python scripts\run_downstream_forecasting.py --input-csv data\raw\<dataset>.csv --time-column <timestamp_column> --columns node_a,node_b,node_c,node_d --dataset-name <dataset_name>
```

## Outputs

Forecasting:

- `results/tables/downstream_forecasting_detail.csv`
- `results/tables/downstream_forecasting_summary.csv`
- `results/tables/downstream_forecasting_summary.md`
- `results/figures/downstream_forecasting_rmse.png`

Graph diagnostics:

- `results/tables/downstream_graph_top_edges.csv`
- `results/tables/downstream_graph_states.csv`
- `results/tables/downstream_graph_diagnostics.md`

Configuration template:

- `configs/real_benchmark_template.yaml`

## Interpretation Rules

- Treat forecasting as supporting evidence, not proof of recovered causal structure.
- Compare STCG-v1 graph masking against dense ridge, random graph masking, and DynVAR-Lasso graph masking.
- Inspect top learned edges for domain plausibility.
- Inspect inferred state windows for regime-like behavior.
- If downstream gains are small, report that directly and emphasize graph diagnostics or limitations.

## Audit Template

For each real dataset run, create a new audit file under `docs/audit/` with:

- dataset source and local filename,
- selected columns and row count,
- missing-value strategy,
- train/test split settings,
- forecasting summary,
- top learned edges,
- state diagnostic summary,
- limitations and any suspected leakage risks.
