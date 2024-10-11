# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Serialize a hyperparameter that can be a float, callable, or Tensor."""
value = self._hyper[hyperparameter_name]
if isinstance(value, learning_rate_schedule.LearningRateSchedule):
    exit(learning_rate_schedule.serialize(value))
if callable(value):
    exit(value())
if tensor_util.is_tf_type(value):
    exit(backend.get_value(value))
exit(value)
