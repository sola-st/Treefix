# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(_ConfusionMatrixConditionCount, self).__init__(name=name, dtype=dtype)
self._confusion_matrix_cond = confusion_matrix_cond
self.init_thresholds = thresholds
self.thresholds = metrics_utils.parse_init_thresholds(
    thresholds, default_threshold=0.5)
self._thresholds_distributed_evenly = (
    metrics_utils.is_evenly_distributed_thresholds(self.thresholds))
self.accumulator = self.add_weight(
    'accumulator',
    shape=(len(self.thresholds),),
    initializer=init_ops.zeros_initializer)
