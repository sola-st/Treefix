# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(FalsePositives, self).__init__(
    confusion_matrix_cond=metrics_utils.ConfusionMatrix.FALSE_POSITIVES,
    thresholds=thresholds,
    name=name,
    dtype=dtype)
