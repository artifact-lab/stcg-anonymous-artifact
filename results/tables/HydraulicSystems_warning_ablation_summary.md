# Hydraulic Warning STCG Selector Ablation

Configurations are selected by `validation_threshold_metric` on the chronological validation segment.
The table reports held-out test metrics for those validation-selected configurations.

| Label | Horizon | Method | Objective | Lookback | Window | Validation F1 | AP | F1 | ROC AUC | State K | Active Dyn. |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| stable_flag | 3 | STCG-v1 Selected Logistic | transition | 40 | 16 | 0.264 | 0.070 | 0.068 | 0.443 | `4:2162` | 8 |
| stable_flag | 3 | Sensor+STCG-v1 Logistic | transition | 40 | 24 | 0.232 | 0.097 | 0.169 | 0.568 | `3:2162` | 6 |
| stable_flag | 5 | STCG-v1 Selected Logistic | stable | 40 | 16 | 0.289 | 0.133 | 0.127 | 0.464 | `1:733;2:1427` | 12 |
| stable_flag | 5 | Sensor+STCG-v1 Logistic | transition | 30 | 24 | 0.359 | 0.180 | 0.216 | 0.587 | `2:2170` | 4 |
| stable_flag | 10 | STCG-v1 Selected Logistic | stable | 40 | 24 | 0.400 | 0.246 | 0.408 | 0.547 | `1:2155` | 0 |
| stable_flag | 10 | Sensor+STCG-v1 Logistic | stable | 30 | 24 | 0.486 | 0.302 | 0.419 | 0.604 | `1:2165` | 0 |
| valve_condition | 3 | STCG-v1 Selected Logistic | stable | 60 | 24 | 0.380 | 0.255 | 0.304 | 0.534 | `1:21;2:1566;3:432;4:123` | 18 |
| valve_condition | 3 | Sensor+STCG-v1 Logistic | stable | 60 | 16 | 0.450 | 0.223 | 0.126 | 0.487 | `1:242;2:1132;3:467;4:301` | 18 |
| valve_condition | 5 | STCG-v1 Selected Logistic | stable | 60 | 16 | 0.542 | 0.382 | 0.472 | 0.504 | `1:242;2:1131;3:466;4:301` | 18 |
| valve_condition | 5 | Sensor+STCG-v1 Logistic | transition | 60 | 16 | 0.585 | 0.362 | 0.526 | 0.492 | `2:5;3:363;4:1772` | 18 |
| valve_condition | 10 | STCG-v1 Selected Logistic | stable | 60 | 24 | 0.864 | 0.772 | 0.524 | 0.486 | `1:21;2:1560;3:432;4:122` | 18 |
| valve_condition | 10 | Sensor+STCG-v1 Logistic | stable | 60 | 24 | 0.862 | 0.840 | 0.671 | 0.618 | `1:21;2:1560;3:432;4:122` | 18 |
