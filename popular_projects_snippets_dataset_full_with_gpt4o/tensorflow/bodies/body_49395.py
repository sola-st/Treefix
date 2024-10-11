# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(SumOverBatchSize, self).__init__(
    reduction=metrics_utils.Reduction.SUM_OVER_BATCH_SIZE,
    name=name,
    dtype=dtype)
