# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""set hyper `name` to value. value can be callable, tensor, numeric."""
if isinstance(value, trackable.Trackable):
    self._track_trackable(value, name, overwrite=True)
if name not in self._hyper:
    self._hyper[name] = value
else:
    prev_value = self._hyper[name]
    if (callable(prev_value)
        or isinstance(prev_value,
                      (ops.Tensor, int, float,
                       learning_rate_schedule.LearningRateSchedule))
        or isinstance(value, learning_rate_schedule.LearningRateSchedule)):
        self._hyper[name] = value
    else:
        backend.set_value(self._hyper[name], value)
