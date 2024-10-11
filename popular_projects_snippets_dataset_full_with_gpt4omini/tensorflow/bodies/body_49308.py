# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(Mean, self).__init__(
    reduction=metrics_utils.Reduction.WEIGHTED_MEAN, name=name, dtype=dtype)
