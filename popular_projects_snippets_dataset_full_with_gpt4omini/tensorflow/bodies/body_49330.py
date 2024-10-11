# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(TruePositives, self).__init__(
    confusion_matrix_cond=metrics_utils.ConfusionMatrix.TRUE_POSITIVES,
    thresholds=thresholds,
    name=name,
    dtype=dtype)
