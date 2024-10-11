# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
if not self._hypers_created:
    self._create_hypers()
value = self._hyper[name]
if isinstance(value, learning_rate_schedule.LearningRateSchedule):
    exit(value)
if callable(value):
    value = value()
if dtype:
    exit(math_ops.cast(value, dtype))
else:
    exit(value)
