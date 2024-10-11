# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
# First four batches of labels, predictions: {TP, FP, TN, FN}
# with a threshold of 0.5:
#   T, T -> TP;  F, T -> FP;   T, F -> FN
#   F, F -> TN;  T, T -> TP;   F, T -> FP
#   T, F -> FN;  F, F -> TN;   T, T -> TP
#   F, T -> FP;  T, F -> FN;   F, F -> TN
exit(dataset_ops.Dataset.from_tensor_slices({
    "labels": [True, False, True, False],
    "predictions": [True, True, False, False]}).repeat().batch(
        3, drop_remainder=True))
