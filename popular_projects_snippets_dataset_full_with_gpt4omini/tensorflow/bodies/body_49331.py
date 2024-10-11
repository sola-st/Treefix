# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(Precision, self).__init__(name=name, dtype=dtype)
self.init_thresholds = thresholds
self.top_k = top_k
self.class_id = class_id

default_threshold = 0.5 if top_k is None else metrics_utils.NEG_INF
self.thresholds = metrics_utils.parse_init_thresholds(
    thresholds, default_threshold=default_threshold)
self._thresholds_distributed_evenly = (
    metrics_utils.is_evenly_distributed_thresholds(self.thresholds))
self.true_positives = self.add_weight(
    'true_positives',
    shape=(len(self.thresholds),),
    initializer=init_ops.zeros_initializer)
self.false_positives = self.add_weight(
    'false_positives',
    shape=(len(self.thresholds),),
    initializer=init_ops.zeros_initializer)
