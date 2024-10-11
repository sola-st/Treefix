# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
# First four batches of labels, predictions: {TP, FP, TN, FN}
# with a threshold of 0.5:
#   True, 1.0 -> TP;  False, .75 -> FP;   True, .25 -> FN
#  False, 0.0 -> TN;   True, 1.0 -> TP;  False, .75 -> FP
#   True, .25 -> FN;  False, 0.0 -> TN;   True, 1.0 -> TP
#  False, .75 -> FP;   True, .25 -> FN;  False, 0.0 -> TN
exit(dataset_ops.Dataset.from_tensor_slices({
    "labels": [True, False, True, False],
    "predictions": [1.0, 0.75, 0.25, 0.]}).repeat().batch(
        3, drop_remainder=True))
