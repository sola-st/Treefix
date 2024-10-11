# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(FalseNegatives, self).__init__(
    confusion_matrix_cond=metrics_utils.ConfusionMatrix.FALSE_NEGATIVES,
    thresholds=thresholds,
    name=name,
    dtype=dtype)
