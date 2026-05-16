# Anonymous STCG Artifact

This is an anonymized reviewer-facing artifact for the submitted CIKM 2026 paper
"Lag-Aware Self-Supervised Dynamic Graph Structure Discovery for Multivariate Time Series."

The package contains code, configuration files, paper source, reproduction instructions,
and tracked result tables/figures. It intentionally omits local raw datasets, processed
label files, Git history, and local build intermediates.

## Contents

- `src/stcg/`: reusable synthetic generation, baseline, recovery, state, and forecasting utilities.
- `scripts/`: experiment entry points for synthetic recovery, real-data diagnostics, ablations, and summaries.
- `configs/`: default synthetic and real benchmark configurations.
- `paper/`: anonymous manuscript source, references, and the generated anonymous PDF when available.
- `results/tables/`: tracked result tables used by the manuscript and reproduction manifest.
- `results/figures/`: tracked figures used by the manuscript and diagnostics.
- `docs/reproduction_manifest.md`: command-level reproduction record for the current checkpoint.
- `docs/real_data_ingestion_checklist.md`: public real-data ingestion requirements and checklist.

## Environment

Python 3.10 or newer is recommended. Install the Python dependencies with:

```powershell
python -m pip install -r requirements.txt
```

For manuscript compilation, use TeX Live or an equivalent LaTeX installation with the ACM
`acmart` class.

## Quick Verification

```powershell
python -m compileall src scripts tests
python -m pytest -q
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/main.tex
bibtex paper/main
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/main.tex
```

The expected Python test status for this package is `48 passed`.

## Main Synthetic Recovery

```powershell
python scripts\run_synthetic_recovery.py --seeds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 --n-nodes 8 --timesteps 1000 --max-lag 3 --window-size 300 --window-stride 150 --window-aggregate max
```

This regenerates the main synthetic recovery tables and figure, including the global and
dynamic Granger-F baseline family.
The focused PCMCI-ParCorr comparison is regenerated with:

```powershell
python scripts\run_synthetic_pcmci_baseline.py --seeds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 --n-nodes 8 --timesteps 1000 --max-lag 3 --window-size 300 --window-stride 150 --window-aggregate max
python scripts\compare_recovery_methods.py --detail-csv results\tables\synthetic_pcmci_baseline_detail.csv --generators var nonlinear_var switching_var --method-a STCG-v1 --method-b PCMCI-ParCorr --output-prefix synthetic_recovery_paired_pcmci_comparison --latex-generator switching_var
```

## Mechanism and Boundary Checks

```powershell
python scripts\run_synthetic_state_oracle.py --seeds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
python scripts\run_synthetic_switch_difficulty.py --seeds 0 1 2 3 4 5 6 7 8 9 --switch-periods 150 300 600
```

The first command compares inferred STCG graph-state aggregation with a synthetic oracle-regime
upper bound. The second command varies the regime switch period to expose when sliding windows
become too mixed for state aggregation to help.

## Forward Real-State Check

```powershell
python scripts\run_real_state_label_prediction_forward.py --input-csv data\raw\HydraulicSystems.csv --labels-csv data\processed\HydraulicSystems_labels.csv --dataset-name HydraulicSystems_forward --label-column cooler_condition --columns TS1,TS2,TS3,TS4,VS1,CE,CP,SE --window-size 300 --window-stride 150 --stcg-v1-states 3 --stcg-v1-force-states --train-fraction 0.80 --seeds 0 1 2 3 4
python scripts\run_real_state_label_prediction_forward.py --input-csv data\raw\HydraulicSystems.csv --labels-csv data\processed\HydraulicSystems_labels.csv --dataset-name HydraulicSystems_valve_forward --label-column valve_condition --columns TS1,TS2,TS3,TS4,VS1,CE,CP,SE --window-size 300 --window-stride 150 --stcg-v1-states 4 --stcg-v1-force-states --train-fraction 0.80 --seeds 0 1 2 3 4
```

These checks fit graph-state centroids and label mappings only on chronological train windows,
then evaluate future windows. They are diagnostic checks, not deployment claims.

## Data Policy

Raw public datasets are not included in this anonymous package. The repository includes
fetching and ingestion scripts where redistribution is inappropriate or unnecessary. See
`docs/real_data_ingestion_checklist.md` and `docs/reproduction_manifest.md` for commands
and expected outputs.

## Anonymity Notes

This package is exported without Git history. The manuscript uses the ACM anonymous review
mode, and the source package omits local raw data, local build logs, local paths, and planning
materials that are not needed for review.
