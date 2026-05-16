# Hydraulic Transition Warning

Features are computed only from past cycles. The target is whether the selected label changes within the next horizon cycles.
Decision thresholds are selected on the chronological validation segment.

| Label | Horizon | Method | Threshold | Test Pos. Rate | Balanced Acc. | Precision | Recall | F1 | AP | ROC AUC |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| valve_condition | 3 | Train Majority | 0.194 | 0.222 | 0.500 | 0.222 | 1.000 | 0.363 | 0.222 | 0.500 |
| valve_condition | 3 | Sensor Logistic | 0.205 | 0.222 | 0.500 | 0.222 | 1.000 | 0.363 | 0.222 | 0.487 |
| valve_condition | 3 | Graph Ridge Logistic | 0.114 | 0.222 | 0.522 | 0.232 | 0.799 | 0.359 | 0.225 | 0.524 |
| valve_condition | 3 | Sensor+Graph Logistic | 0.045 | 0.222 | 0.496 | 0.220 | 0.944 | 0.357 | 0.230 | 0.538 |
| valve_condition | 3 | STCG-v1 Selected Logistic | 0.565 | 0.222 | 0.509 | 0.231 | 0.361 | 0.282 | 0.237 | 0.541 |
| valve_condition | 3 | Sensor+STCG-v1 Logistic | 0.741 | 0.222 | 0.528 | 0.261 | 0.292 | 0.275 | 0.239 | 0.537 |
| valve_condition | 5 | Train Majority | 0.324 | 0.370 | 0.500 | 0.370 | 1.000 | 0.541 | 0.370 | 0.500 |
| valve_condition | 5 | Sensor Logistic | 0.172 | 0.370 | 0.500 | 0.370 | 1.000 | 0.541 | 0.404 | 0.520 |
| valve_condition | 5 | Graph Ridge Logistic | 0.205 | 0.370 | 0.554 | 0.409 | 0.721 | 0.522 | 0.411 | 0.554 |
| valve_condition | 5 | Sensor+Graph Logistic | 0.010 | 0.370 | 0.527 | 0.385 | 0.904 | 0.540 | 0.425 | 0.568 |
| valve_condition | 5 | STCG-v1 Selected Logistic | 0.001 | 0.370 | 0.509 | 0.374 | 1.000 | 0.545 | 0.380 | 0.543 |
| valve_condition | 5 | Sensor+STCG-v1 Logistic | 0.026 | 0.370 | 0.524 | 0.383 | 0.938 | 0.543 | 0.388 | 0.557 |
| valve_condition | 10 | Train Majority | 0.650 | 0.742 | 0.500 | 0.742 | 1.000 | 0.852 | 0.742 | 0.500 |
| valve_condition | 10 | Sensor Logistic | 0.101 | 0.742 | 0.500 | 0.742 | 1.000 | 0.852 | 0.852 | 0.646 |
| valve_condition | 10 | Graph Ridge Logistic | 0.031 | 0.742 | 0.655 | 0.816 | 0.879 | 0.847 | 0.899 | 0.762 |
| valve_condition | 10 | Sensor+Graph Logistic | 0.002 | 0.742 | 0.504 | 0.743 | 0.996 | 0.851 | 0.909 | 0.771 |
| valve_condition | 10 | STCG-v1 Selected Logistic | 0.000 | 0.742 | 0.523 | 0.751 | 0.985 | 0.852 | 0.793 | 0.590 |
| valve_condition | 10 | Sensor+STCG-v1 Logistic | 0.000 | 0.742 | 0.518 | 0.749 | 1.000 | 0.856 | 0.789 | 0.606 |
| stable_flag | 3 | Train Majority | 0.076 | 0.082 | 0.500 | 0.082 | 1.000 | 0.151 | 0.082 | 0.500 |
| stable_flag | 3 | Sensor Logistic | 0.374 | 0.082 | 0.549 | 0.156 | 0.189 | 0.171 | 0.113 | 0.583 |
| stable_flag | 3 | Graph Ridge Logistic | 0.974 | 0.082 | 0.514 | 0.091 | 0.245 | 0.133 | 0.134 | 0.583 |
| stable_flag | 3 | Sensor+Graph Logistic | 0.965 | 0.082 | 0.517 | 0.090 | 0.321 | 0.141 | 0.117 | 0.586 |
| stable_flag | 3 | STCG-v1 Selected Logistic | 0.147 | 0.082 | 0.542 | 0.095 | 0.547 | 0.162 | 0.084 | 0.520 |
| stable_flag | 3 | Sensor+STCG-v1 Logistic | 0.011 | 0.082 | 0.559 | 0.095 | 0.774 | 0.169 | 0.097 | 0.568 |
| stable_flag | 5 | Train Majority | 0.119 | 0.128 | 0.500 | 0.128 | 1.000 | 0.227 | 0.128 | 0.500 |
| stable_flag | 5 | Sensor Logistic | 0.744 | 0.128 | 0.524 | 0.167 | 0.181 | 0.173 | 0.155 | 0.545 |
| stable_flag | 5 | Graph Ridge Logistic | 0.025 | 0.128 | 0.510 | 0.132 | 0.542 | 0.213 | 0.114 | 0.478 |
| stable_flag | 5 | Sensor+Graph Logistic | 0.108 | 0.128 | 0.534 | 0.137 | 0.940 | 0.239 | 0.110 | 0.468 |
| stable_flag | 5 | STCG-v1 Selected Logistic | 0.053 | 0.128 | 0.519 | 0.135 | 0.614 | 0.222 | 0.138 | 0.528 |
| stable_flag | 5 | Sensor+STCG-v1 Logistic | 0.015 | 0.128 | 0.516 | 0.132 | 0.855 | 0.229 | 0.165 | 0.558 |
| stable_flag | 10 | Train Majority | 0.228 | 0.244 | 0.500 | 0.244 | 1.000 | 0.393 | 0.244 | 0.500 |
| stable_flag | 10 | Sensor Logistic | 0.277 | 0.244 | 0.500 | 0.244 | 1.000 | 0.393 | 0.256 | 0.483 |
| stable_flag | 10 | Graph Ridge Logistic | 0.000 | 0.244 | 0.527 | 0.256 | 0.911 | 0.399 | 0.269 | 0.525 |
| stable_flag | 10 | Sensor+Graph Logistic | 0.000 | 0.244 | 0.534 | 0.258 | 0.937 | 0.405 | 0.268 | 0.536 |
| stable_flag | 10 | STCG-v1 Selected Logistic | 0.263 | 0.244 | 0.566 | 0.283 | 0.734 | 0.408 | 0.245 | 0.545 |
| stable_flag | 10 | Sensor+STCG-v1 Logistic | 0.005 | 0.244 | 0.563 | 0.271 | 0.968 | 0.423 | 0.265 | 0.584 |
