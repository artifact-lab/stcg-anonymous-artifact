# Reproduction Manifest

Last updated: 2026-05-17 Asia/Shanghai.

This manifest records the commands needed to regenerate the current STCG baseline artifacts from the repository root.

## Environment

Recommended runtime:

- Python 3.10+
- TeX Live with `acmart`
- Python packages from `requirements.txt` or `pyproject.toml`

Quick verification:

```powershell
python -m compileall src scripts tests
python -m pytest -q
```

Expected status at this checkpoint:

- `pytest`: 48 passed.
- `compileall`: passes for `src`, `scripts`, and `tests`.

## Synthetic Recovery

Main recovery table and figure:

```powershell
python scripts\run_synthetic_recovery.py --seeds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 --n-nodes 8 --timesteps 1000 --max-lag 3 --window-size 300 --window-stride 150 --window-aggregate max
```

This main recovery run includes the strong conditional Granger family: global `Granger-F` and dynamic-window `DynGranger-F`.

Outputs:

- `results/tables/synthetic_recovery_detail.csv`
- `results/tables/synthetic_recovery_summary.csv`
- `results/tables/synthetic_recovery_summary.md`
- `results/tables/synthetic_recovery_table.tex`
- `results/figures/synthetic_recovery_edge_auc.png`

Focused PCMCI-ParCorr baseline comparison:

```powershell
python scripts\run_synthetic_pcmci_baseline.py --seeds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 --n-nodes 8 --timesteps 1000 --max-lag 3 --window-size 300 --window-stride 150 --window-aggregate max
python scripts\compare_recovery_methods.py --detail-csv results\tables\synthetic_pcmci_baseline_detail.csv --generators var nonlinear_var switching_var --method-a STCG-v1 --method-b PCMCI-ParCorr --output-prefix synthetic_recovery_paired_pcmci_comparison --latex-generator switching_var
```

Outputs:

- `results/tables/synthetic_pcmci_baseline_detail.csv`
- `results/tables/synthetic_pcmci_baseline_summary.csv`
- `results/tables/synthetic_pcmci_baseline_summary.md`
- `results/tables/synthetic_pcmci_baseline_table.tex`
- `results/figures/synthetic_pcmci_baseline_edge_auc.png`
- `results/tables/synthetic_recovery_paired_pcmci_comparison_detail.csv`
- `results/tables/synthetic_recovery_paired_pcmci_comparison_summary.csv`
- `results/tables/synthetic_recovery_paired_pcmci_comparison_summary.md`
- `results/tables/synthetic_recovery_paired_pcmci_comparison_table.tex`

Paired STCG-v1 vs DynVAR-Lasso comparison:

```powershell
python scripts\compare_recovery_methods.py --generators var nonlinear_var switching_var --method-a STCG-v1 --method-b DynVAR-Lasso
```

Outputs:

- `results/tables/synthetic_recovery_paired_comparison_detail.csv`
- `results/tables/synthetic_recovery_paired_comparison_summary.csv`
- `results/tables/synthetic_recovery_paired_comparison_summary.md`
- `results/tables/synthetic_recovery_paired_comparison_table.tex`

Paired STCG-v1 vs DynGranger-F comparison:

```powershell
python scripts\compare_recovery_methods.py --generators var nonlinear_var switching_var --method-a STCG-v1 --method-b DynGranger-F --output-prefix synthetic_recovery_paired_granger_comparison --latex-generator switching_var
```

Outputs:

- `results/tables/synthetic_recovery_paired_granger_comparison_detail.csv`
- `results/tables/synthetic_recovery_paired_granger_comparison_summary.csv`
- `results/tables/synthetic_recovery_paired_granger_comparison_summary.md`
- `results/tables/synthetic_recovery_paired_granger_comparison_table.tex`

## STCG-v1 Ablation

```powershell
python scripts\run_stcg_ablation.py --seeds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 --n-nodes 8 --timesteps 1000 --max-lag 3 --window-size 300 --window-stride 150
```

Outputs:

- `results/tables/stcg_v1_ablation_detail.csv`
- `results/tables/stcg_v1_ablation_summary.csv`
- `results/tables/stcg_v1_ablation_summary.md`
- `results/tables/stcg_v1_ablation_table.tex`
- `results/figures/stcg_v1_ablation_edge_auc.png`

## STCG-v1 Oracle-State Mechanism Check

```powershell
python scripts\run_synthetic_state_oracle.py --seeds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
```

This diagnostic compares STCG-v1 inferred graph-state aggregation with an oracle-state upper bound
that uses the true synthetic regime label only after local window scoring. It is not a supervised
training variant.

Outputs:

- `results/tables/synthetic_state_oracle_detail.csv`
- `results/tables/synthetic_state_oracle_summary.csv`
- `results/tables/synthetic_state_oracle_summary.md`
- `results/tables/synthetic_state_oracle_table.tex`
- `results/figures/synthetic_state_oracle_edge_auc.png`

## Synthetic Switch-Difficulty Sweep

```powershell
python scripts\run_synthetic_switch_difficulty.py --seeds 0 1 2 3 4 5 6 7 8 9 --switch-periods 150 300 600
```

This boundary check varies the regime switch period while keeping the sliding-window setup fixed.
Short periods create mixed windows and are expected to reduce the benefit of state aggregation.

Outputs:

- `results/tables/synthetic_switch_difficulty_detail.csv`
- `results/tables/synthetic_switch_difficulty_summary.csv`
- `results/tables/synthetic_switch_difficulty_summary.md`
- `results/tables/synthetic_switch_difficulty_table.tex`
- `results/figures/synthetic_switch_difficulty_edge_auc.png`

## STCG-v1 Robustness

```powershell
python scripts\run_stcg_robustness.py --seeds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
```

Outputs:

- `results/tables/stcg_v1_robustness_detail.csv`
- `results/tables/stcg_v1_robustness_summary.csv`
- `results/tables/stcg_v1_robustness_summary.md`
- `results/tables/stcg_v1_robustness_table.tex`
- `results/figures/stcg_v1_robustness_edge_auc.png`

## State Diagnostics

```powershell
python scripts\run_stcg_state_diagnostics.py --seeds 0 1 2 3 4 --plot-seed 0
```

Outputs:

- `results/tables/stcg_v1_state_diagnostics_detail.csv`
- `results/tables/stcg_v1_state_diagnostics_summary.csv`
- `results/tables/stcg_v1_state_diagnostics_summary.md`
- `results/figures/stcg_v1_state_diagnostics_seed0.png`

## Downstream Forecasting Harness

Synthetic switching smoke run:

```powershell
python scripts\run_downstream_forecasting.py --seeds 0 1 2 3 4
```

Outputs:

- `results/tables/downstream_forecasting_detail.csv`
- `results/tables/downstream_forecasting_summary.csv`
- `results/tables/downstream_forecasting_summary.md`
- `results/figures/downstream_forecasting_rmse.png`
- `results/tables/downstream_graph_top_edges.csv`
- `results/tables/downstream_graph_states.csv`
- `results/tables/downstream_graph_diagnostics.md`

Local CSV entry point:

```powershell
python scripts\fetch_ett_benchmarks.py
python scripts\fetch_beijing_air_quality.py
python scripts\fetch_uci_occupancy.py
python scripts\fetch_uci_arem.py
python scripts\fetch_uci_har.py
# Preferred real operating-mode candidate. The full UCI/Zenodo zip can be used when the network allows it.
python scripts\fetch_hydraulic_systems.py --force
# Current 2026-05-15 checkpoint used a GitHub-mirror low-frequency subset zip named hydraulic_systems_lowfreq.zip.
python scripts\fetch_hydraulic_systems.py --zip-name hydraulic_systems_lowfreq.zip --sensors TS1,TS2,TS3,TS4,VS1,CE,CP,SE --source-url https://github.com/DrewAlderfer/hydraulic_pump_monitoring/tree/main/data --skip-md5-check
python scripts\check_real_data_inventory.py
python scripts\run_real_benchmark_from_inventory.py
python scripts\run_downstream_forecasting.py --input-csv data\raw\your_timeseries.csv --time-column timestamp --dataset-name your_dataset
```

Inventory outputs:

- `results/tables/real_data_inventory.csv`
- `results/tables/real_data_inventory.md`
- `results/tables/real_benchmark_run_plan.md`

The CSV runner learns graph scores only from the training segment and evaluates one-step prediction on held-out future samples.
It reports both hard graph-mask ridge and soft graph-weighted ridge; the soft version keeps all lagged features and uses graph scores as diagonal ridge-prior weights.
Use `configs/real_benchmark_template.yaml` to record dataset-specific settings before reporting a real-data result.
`scripts\fetch_hydraulic_systems.py` supports the UCI Hydraulic Systems candidate. The 2026-05-15 checkpoint recovered the data through a public GitHub mirror and prepared the low-frequency/summary sensor subset; see `docs/audit/hydraulic_systems_mode_transfer_2026-05-15.md`.
To run all inventory-approved datasets into ignored per-dataset folders under `experiments/logs/real_benchmarks/`, use:

```powershell
python scripts\run_real_benchmark_from_inventory.py --execute
python scripts\summarize_real_benchmarks.py
```

Real benchmark summary outputs:

- `results/tables/real_benchmark_forecasting_summary.csv`
- `results/tables/real_benchmark_forecasting_summary.md`
- `results/tables/real_benchmark_forecasting_table.tex`
- `results/tables/real_benchmark_top_edges.csv`
- `results/tables/real_benchmark_top_edges.md`
- `results/tables/real_benchmark_state_summary.csv`
- `results/tables/real_benchmark_state_summary.md`

External real-state label alignment for datasets with held-out audit labels:

```powershell
python scripts\compare_real_state_labels.py
python scripts\compare_real_state_labels.py --states-csv experiments\logs\real_benchmarks\AReMActivities\tables\downstream_graph_states.csv --labels-csv data\processed\AReMActivities_labels.csv --dataset-name AReMActivities --label-column activity
python scripts\run_real_state_sensitivity.py
python scripts\run_arem_threshold_forecasting.py
python scripts\run_arem_threshold_forecasting.py --input-csv data\raw\UCIHARWindowSignals.csv --labels-csv data\processed\UCIHARWindowSignals_labels.csv --dataset-name UCIHARWindowSignals --label-column activity --state-counts 2 3 4 --window-size 80 --window-stride 40 --min-improvements 0.0 0.04 0.08 0.12 0.16
python scripts\compare_real_state_labels.py --states-csv experiments\logs\real_benchmarks\HydraulicSystems\tables\downstream_graph_states.csv --labels-csv data\processed\HydraulicSystems_labels.csv --dataset-name HydraulicSystems --label-column cooler_condition
python scripts\run_arem_threshold_forecasting.py --input-csv data\raw\HydraulicSystems.csv --labels-csv data\processed\HydraulicSystems_labels.csv --dataset-name HydraulicSystems_cooler_condition --label-column cooler_condition --columns TS1,TS2,TS3,TS4,VS1,CE,CP,SE --state-counts 2 --min-improvements 0.0 0.08 0.12 0.16 --ridge-alphas 1.0 10.0 100.0 --graph-min-weights 0.01 0.10 --graph-weight-powers 1.0 4.0 --window-size 300 --window-stride 150
```

Outputs:

- `results/tables/OccupancySensors_state_label_alignment_detail.csv`
- `results/tables/OccupancySensors_state_label_alignment_summary.csv`
- `results/tables/OccupancySensors_state_label_alignment_summary.md`
- `results/figures/OccupancySensors_state_label_alignment_seed0.png`
- `results/tables/AReMActivities_state_label_alignment_detail.csv`
- `results/tables/AReMActivities_state_label_alignment_summary.csv`
- `results/tables/AReMActivities_state_label_alignment_summary.md`
- `results/tables/AReMActivities_state_sensitivity_summary.csv`
- `results/tables/AReMActivities_state_sensitivity_summary.md`
- `results/tables/AReMActivities_state_threshold_forecasting_detail.csv`
- `results/tables/AReMActivities_state_threshold_forecasting_summary.csv`
- `results/tables/AReMActivities_state_threshold_forecasting_summary.md`
- `results/tables/UCIHARWindowSignals_state_label_alignment_detail.csv`
- `results/tables/UCIHARWindowSignals_state_label_alignment_summary.csv`
- `results/tables/UCIHARWindowSignals_state_label_alignment_summary.md`
- `results/tables/UCIHARWindowSignals_state_threshold_forecasting_detail.csv`
- `results/tables/UCIHARWindowSignals_state_threshold_forecasting_summary.csv`
- `results/tables/UCIHARWindowSignals_state_threshold_forecasting_summary.md`
- `results/tables/HydraulicSystems_state_label_alignment_detail.csv`
- `results/tables/HydraulicSystems_state_label_alignment_summary.csv`
- `results/tables/HydraulicSystems_state_label_alignment_summary.md`
- `results/tables/HydraulicSystems_state_threshold_forecasting_detail.csv`
- `results/tables/HydraulicSystems_state_threshold_forecasting_summary.csv`
- `results/tables/HydraulicSystems_state_threshold_forecasting_summary.md`
- `results/tables/HydraulicSystems_cooler_condition_state_threshold_forecasting_detail.csv`
- `results/tables/HydraulicSystems_cooler_condition_state_threshold_forecasting_summary.csv`
- `results/tables/HydraulicSystems_cooler_condition_state_threshold_forecasting_summary.md`
- `results/figures/UCIHARWindowSignals_state_label_alignment_seed0.png`
- `results/figures/AReMActivities_state_label_alignment_seed0.png`
- `results/figures/HydraulicSystems_state_label_alignment_seed0.png`

Real state-label prediction beyond one-step forecasting:

```powershell
python scripts\run_real_state_label_prediction.py --input-csv data\raw\HydraulicSystems.csv --labels-csv data\processed\HydraulicSystems_labels.csv --dataset-name HydraulicSystems --label-column cooler_condition --columns TS1,TS2,TS3,TS4,VS1,CE,CP,SE --window-size 300 --window-stride 150
python scripts\run_real_state_label_prediction.py --input-csv data\raw\HydraulicSystems.csv --labels-csv data\processed\HydraulicSystems_labels.csv --dataset-name HydraulicSystems_cooler_K3 --label-column cooler_condition --columns TS1,TS2,TS3,TS4,VS1,CE,CP,SE --window-size 300 --window-stride 150 --stcg-v1-states 3
python scripts\run_real_state_label_prediction.py --input-csv data\raw\AReMActivities.csv --labels-csv data\processed\AReMActivities_labels.csv --dataset-name AReMActivities_K4 --label-column activity --columns avg_rss12,var_rss12,avg_rss13,var_rss13,avg_rss23,var_rss23 --window-size 300 --window-stride 150 --stcg-v1-states 4
python scripts\run_real_state_count_selection.py --input-csv data\raw\HydraulicSystems.csv --labels-csv data\processed\HydraulicSystems_labels.csv --dataset-name HydraulicSystems_cooler_selectK --label-column cooler_condition --columns TS1,TS2,TS3,TS4,VS1,CE,CP,SE --window-size 300 --window-stride 150 --state-counts 1 2 3 4 5 6
python scripts\run_real_state_count_selection.py --input-csv data\raw\AReMActivities.csv --labels-csv data\processed\AReMActivities_labels.csv --dataset-name AReMActivities_selectK --label-column activity --columns avg_rss12,var_rss12,avg_rss13,var_rss13,avg_rss23,var_rss23 --window-size 300 --window-stride 150 --state-counts 1 2 3 4 5 6
python scripts\run_real_state_label_prediction_forward.py --input-csv data\raw\HydraulicSystems.csv --labels-csv data\processed\HydraulicSystems_labels.csv --dataset-name HydraulicSystems_forward --label-column cooler_condition --columns TS1,TS2,TS3,TS4,VS1,CE,CP,SE --window-size 300 --window-stride 150 --stcg-v1-states 3 --stcg-v1-force-states --train-fraction 0.80 --seeds 0 1 2 3 4
python scripts\run_real_state_label_prediction_forward.py --input-csv data\raw\HydraulicSystems.csv --labels-csv data\processed\HydraulicSystems_labels.csv --dataset-name HydraulicSystems_valve_forward --label-column valve_condition --columns TS1,TS2,TS3,TS4,VS1,CE,CP,SE --window-size 300 --window-stride 150 --stcg-v1-states 4 --stcg-v1-force-states --train-fraction 0.80 --seeds 0 1 2 3 4
python scripts\run_hydraulic_transition_warning.py --input-csv data\raw\HydraulicSystems.csv --labels-csv data\processed\HydraulicSystems_labels.csv --dataset-name HydraulicSystems --label-columns valve_condition stable_flag --columns TS1,TS2,TS3,TS4,VS1,CE,CP,SE --horizon-cycles 3 5 10 --lookback-cycles 40
python scripts\run_hydraulic_warning_ablation.py --input-csv data\raw\HydraulicSystems.csv --labels-csv data\processed\HydraulicSystems_labels.csv --dataset-name HydraulicSystems --label-columns valve_condition stable_flag --columns TS1,TS2,TS3,TS4,VS1,CE,CP,SE --horizon-cycles 3 5 10 --lookback-cycles 30 40 60 --selection-objectives stable transition --stcg-window-sizes 16 24 --stcg-window-strides 8
```

Outputs:

- `results/tables/HydraulicSystems_state_label_prediction_detail.csv`
- `results/tables/HydraulicSystems_state_label_prediction_summary.csv`
- `results/tables/HydraulicSystems_state_label_prediction_summary.md`
- `results/figures/HydraulicSystems_state_label_prediction_balanced_accuracy.png`
- `results/tables/HydraulicSystems_cooler_K3_state_label_prediction_detail.csv`
- `results/tables/HydraulicSystems_cooler_K3_state_label_prediction_summary.csv`
- `results/tables/HydraulicSystems_cooler_K3_state_label_prediction_summary.md`
- `results/figures/HydraulicSystems_cooler_K3_state_label_prediction_balanced_accuracy.png`
- `results/tables/AReMActivities_K4_state_label_prediction_detail.csv`
- `results/tables/AReMActivities_K4_state_label_prediction_summary.csv`
- `results/tables/AReMActivities_K4_state_label_prediction_summary.md`
- `results/figures/AReMActivities_K4_state_label_prediction_balanced_accuracy.png`
- `results/tables/HydraulicSystems_cooler_selectK_state_count_selection_detail.csv`
- `results/tables/HydraulicSystems_cooler_selectK_state_count_selection_summary.csv`
- `results/tables/HydraulicSystems_cooler_selectK_state_count_selection_selected.csv`
- `results/tables/HydraulicSystems_cooler_selectK_state_count_selection_summary.md`
- `results/figures/HydraulicSystems_cooler_selectK_state_count_selection.png`
- `results/tables/AReMActivities_selectK_state_count_selection_detail.csv`
- `results/tables/AReMActivities_selectK_state_count_selection_summary.csv`
- `results/tables/AReMActivities_selectK_state_count_selection_selected.csv`
- `results/tables/AReMActivities_selectK_state_count_selection_summary.md`
- `results/figures/AReMActivities_selectK_state_count_selection.png`
- `results/tables/HydraulicSystems_forward_state_label_prediction_forward_detail.csv`
- `results/tables/HydraulicSystems_forward_state_label_prediction_forward_summary.csv`
- `results/tables/HydraulicSystems_forward_state_label_prediction_forward_summary.md`
- `results/figures/HydraulicSystems_forward_state_label_prediction_forward_balanced_accuracy.png`
- `results/tables/HydraulicSystems_valve_forward_state_label_prediction_forward_detail.csv`
- `results/tables/HydraulicSystems_valve_forward_state_label_prediction_forward_summary.csv`
- `results/tables/HydraulicSystems_valve_forward_state_label_prediction_forward_summary.md`
- `results/figures/HydraulicSystems_valve_forward_state_label_prediction_forward_balanced_accuracy.png`
- `results/tables/HydraulicSystems_transition_warning_detail.csv`
- `results/tables/HydraulicSystems_transition_warning_summary.md`
- `results/tables/HydraulicSystems_transition_warning_best.md`
- `results/figures/HydraulicSystems_transition_warning_average_precision.png`
- `results/tables/HydraulicSystems_warning_ablation_detail.csv`
- `results/tables/HydraulicSystems_warning_ablation_selected.csv`
- `results/tables/HydraulicSystems_warning_ablation_summary.md`
- `results/figures/HydraulicSystems_warning_ablation_average_precision.png`

Hard graph-mask sweep:

```powershell
python scripts\run_real_mask_sweep.py --datasets ETTh1 ETTh2
```

Outputs:

- `results/tables/real_mask_sweep_detail.csv`
- `results/tables/real_mask_sweep_summary.csv`
- `results/tables/real_mask_sweep_summary.md`

Soft graph-prior sweep:

```powershell
python scripts\run_real_weight_sweep.py
```

Outputs:

- `results/tables/real_weight_sweep_detail.csv`
- `results/tables/real_weight_sweep_summary.csv`
- `results/tables/real_weight_sweep_summary.md`

## Paper Build

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/main.tex
bibtex paper/main
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/main.tex
```

Output:

- `paper/main.pdf`

The PDF and LaTeX intermediate files are ignored by git to avoid binary and build-output churn.

## Current Evidence Checkpoint

The baseline claim at this checkpoint is deliberately scoped:

- STCG-v1 improves switching-regime lagged structure recovery over dynamic VAR, dynamic Granger, and PCMCI-ParCorr baselines in the 20-seed main run.
- PCMCI-ParCorr is a strong stationary reference: it beats STCG-v1 on stationary VAR and nonlinear VAR, while STCG-v1 beats PCMCI-ParCorr on switching VAR with significant paired Edge AUC, Pair AUC, Precision@K, SHD, and Lag Accuracy gains.
- The oracle-state diagnostic shows that inferred STCG-v1 graph states nearly match the synthetic oracle-regime upper bound on the default switching setup: inferred-state Edge AUC `0.812` versus oracle-state `0.813` and DynVAR-Lasso/no-state `0.798`.
- The switch-difficulty sweep clarifies the boundary condition. With switch period `150`, windows are heavily mixed and STCG-v1 does not improve Edge AUC over DynVAR-Lasso (`0.733` vs `0.733`); with period `600`, STCG-v1 nearly matches oracle-state aggregation (`0.847` vs `0.849`) and improves over DynVAR-Lasso (`0.835`).
- The stronger global Granger-F, VAR-Lasso, and PCMCI-ParCorr baselines remain better on stationary and nonlinear VAR, narrowing the claim to dynamic-structure settings.
- The ablation attributes the gain to latent graph-state aggregation.
- Robustness favors STCG-v1 in sufficiently sampled switching systems.
- State diagnostics show inferred states align with hidden regimes.
- Real ETTh1/ETTh2/ETTm1/ETTm2, BeijingPM25, OccupancySensors, AReMActivities, UCIHARWindowSignals, and HydraulicSystems forecasting is now executed; dense ridge remains a strong ceiling, while OccupancySensors slightly favors persistence below the `0.001` meaningful-gain threshold.
- Soft graph-weighted ridge repairs the hard-mask deletion failure on the earlier real datasets; the eight-dataset weighted-prior sweep finds a meaningful AReMActivities gain (`0.002924` RMSE over tuned dense ridge), while UCIHARWindowSignals improves only `0.000671` RMSE over tuned dense ridge and remains below the meaningful threshold.
- OccupancySensors adds explicit binary occupancy-state labels for audit, but STCG-v1 still collapses to one inferred graph state under the current score-clustering settings; post-hoc label alignment gives ARI `0.000` and aligned accuracy `0.737`, matching the majority label rate rather than a learned state partition.
- AReMActivities adds seven activity labels; default `K=2` now yields non-collapsed temporally coherent states (ARI `0.251 +/- 0.000`), the threshold/forecasting sweep shows `K=3` reaches ARI `0.309 +/- 0.035`, and `K=4` STCG-v1 weighted ridge reaches RMSE `0.904089` versus DynVAR-Lasso weighted ridge `0.906191`.
- The tuned AReM STCG-v1 gain over DynVAR-Lasso is meaningful by the `0.001` RMSE threshold but not statistically confirmed over five seeds (paired t-test `p=0.142`, Wilcoxon one-sided `p=0.0625`).
- UCIHARWindowSignals remains a weak/negative mode-labelled transfer check; default settings collapse to one state, low-threshold non-collapsed settings reach only weak activity alignment (best ARI `0.090 +/- 0.007`), and there is no meaningful STCG-v1 gain over DynVAR-Lasso weighted ridge.
- HydraulicSystems is now the stronger industrial mode-labelled transfer check. The temporal-fallback auto-state objective makes default `K=2` states align with `cooler_condition` (ARI `0.735 +/- 0.006`, aligned accuracy `0.902 +/- 0.002`) without a meaningful forecasting gain over DynVAR-Lasso weighted ridge.
- A label-stratified downstream diagnosis now tests graph states beyond one-step forecasting. On Hydraulic cooler-condition labels, default `K=2` STCG state mapping underfits the three-level label (held-out balanced accuracy `0.656 +/- 0.002`), while `K=3` reaches `0.948 +/- 0.004`; graph-score centroid features reach `0.959 +/- 0.003`, and the simple sensor-feature ceiling reaches `0.994 +/- 0.004`.
- Label-free state-count selection uses `state_improvement * temporal_coherence * balance_score / log2(K + 1)`. It selects `K=3` for Hydraulic in all five seeds, preserving the `0.948 +/- 0.004` held-out balanced accuracy without using labels to choose `K`.
- The same selector picks coarse `K=2` AReM graph states in all five seeds, reaching only `0.283 +/- 0.005` balanced accuracy against seven activity labels. This reinforces that AReM activity classes are not naturally recovered by the compact graph-state objective.
- The forward-only Hydraulic state check fits graph-state centroids and label mappings on chronological train windows only. For cooler-condition late-future windows, STCG-v1 state mapping reaches balanced accuracy `0.953 +/- 0.003`, graph-feature centroids reach `0.966 +/- 0.000`, and the sensor-feature ceiling reaches `1.000 +/- 0.000`; the test segment is single-condition, so this is a leakage-reduction diagnostic rather than a complete multi-class deployment result.
- A forward-only valve-condition check keeps multiple future classes and is deliberately negative for compact states: STCG-v1 state mapping remains at the train-majority level (`0.250` balanced accuracy), while graph-feature centroids reach `0.323`. This keeps the real-data transfer claim bounded.
- A chronological Hydraulic transition-warning pilot now uses only past-cycle features to predict whether a label changes within the next horizon. Thresholds are selected on a chronological validation segment. For 10-cycle `valve_condition` warnings, Sensor+Graph Logistic reaches AP `0.909` and ROC AUC `0.771` versus majority AP `0.742`; for 10-cycle `stable_flag`, Graph Ridge Logistic reaches AP `0.269` versus majority AP `0.244`. Shorter horizons remain weak.
- The same warning harness includes label-free selected STCG-v1 graph-state features. The warning selector now defaults to a transition-oriented multi-state objective and appends explicit state-dynamics features; this prevents the previous one-state collapse in the warning design. STCG-v1 is still mixed: Sensor+STCG-v1 is best by AP on 5-cycle `stable_flag` warnings (`0.165` versus majority AP `0.128`) and 3-cycle `valve_condition` warnings (`0.239` versus majority AP `0.222`), and it has the best F1 on 10-cycle `valve_condition` (`0.856`) and 10-cycle `stable_flag` (`0.423`). Ridge graph features remain stronger on the main 10-cycle `valve_condition` AP result.
- A follow-up warning ablation compares `stable` versus `transition` selectors over lookbacks `30/40/60` and STCG windows `16/24`, selecting configurations only by validation F1. The selected grid improves `Sensor+STCG-v1` on 10-cycle `stable_flag` AP to `0.302`, but the same lookback has Sensor Logistic AP `0.374`; on the main 10-cycle `valve_condition` setting, selected `Sensor+STCG-v1` reaches AP `0.840`, still below Sensor+Graph AP `0.909`.
- The manuscript has been consolidated around this bounded claim: Related Work no longer has placeholders, Method now includes state-selection formulas and Algorithm 1, the real-data protocol explicitly separates unsupervised graph inference, validation selection, and held-out testing, and the synthetic baseline family now includes global and dynamic Granger-F tests plus PCMCI-ParCorr.

The next checkpoint should freeze the baseline set, run final manuscript checks, and move to submission-package readiness.
