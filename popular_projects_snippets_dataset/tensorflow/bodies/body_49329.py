# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(TrueNegatives, self).__init__(
    confusion_matrix_cond=metrics_utils.ConfusionMatrix.TRUE_NEGATIVES,
    thresholds=thresholds,
    name=name,
    dtype=dtype)
