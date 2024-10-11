# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(Reduce, self).__init__(name=name, dtype=dtype)
self.reduction = reduction
self.total = self.add_weight(
    'total', initializer=init_ops.zeros_initializer)
if reduction in [metrics_utils.Reduction.SUM_OVER_BATCH_SIZE,
                 metrics_utils.Reduction.WEIGHTED_MEAN]:
    self.count = self.add_weight(
        'count', initializer=init_ops.zeros_initializer)
