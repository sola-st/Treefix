# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(SensitivitySpecificityBase, self).__init__(name=name, dtype=dtype)
if num_thresholds <= 0:
    raise ValueError('`num_thresholds` must be > 0.')
self.value = value
self.class_id = class_id
self.true_positives = self.add_weight(
    'true_positives',
    shape=(num_thresholds,),
    initializer=init_ops.zeros_initializer)
self.true_negatives = self.add_weight(
    'true_negatives',
    shape=(num_thresholds,),
    initializer=init_ops.zeros_initializer)
self.false_positives = self.add_weight(
    'false_positives',
    shape=(num_thresholds,),
    initializer=init_ops.zeros_initializer)
self.false_negatives = self.add_weight(
    'false_negatives',
    shape=(num_thresholds,),
    initializer=init_ops.zeros_initializer)

# Compute `num_thresholds` thresholds in [0, 1]
if num_thresholds == 1:
    self.thresholds = [0.5]
    self._thresholds_distributed_evenly = False
else:
    thresholds = [(i + 1) * 1.0 / (num_thresholds - 1)
                  for i in range(num_thresholds - 2)]
    self.thresholds = [0.0] + thresholds + [1.0]
    self._thresholds_distributed_evenly = True
