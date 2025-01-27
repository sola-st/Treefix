# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
setattr(self, name, value)
if isinstance(value, trackable_base.Trackable):
    self._track_trackable(value, name)  # pylint:disable=protected-access
