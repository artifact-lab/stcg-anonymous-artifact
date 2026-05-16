# Hydraulic Transition Warning Best Methods

| Label | Horizon | Best Method | Threshold | AP | AP Gain vs Majority | F1 | ROC AUC |
|---|---:|---|---:|---:|---:|---:|---:|
| stable_flag | 3 | Graph Ridge Logistic | 0.974 | 0.134 | 0.052 | 0.133 | 0.583 |
| stable_flag | 5 | Sensor+STCG-v1 Logistic | 0.015 | 0.165 | 0.037 | 0.229 | 0.558 |
| stable_flag | 10 | Graph Ridge Logistic | 0.000 | 0.269 | 0.024 | 0.399 | 0.525 |
| valve_condition | 3 | Sensor+STCG-v1 Logistic | 0.741 | 0.239 | 0.017 | 0.275 | 0.537 |
| valve_condition | 5 | Sensor+Graph Logistic | 0.010 | 0.425 | 0.054 | 0.540 | 0.568 |
| valve_condition | 10 | Sensor+Graph Logistic | 0.002 | 0.909 | 0.167 | 0.851 | 0.771 |
