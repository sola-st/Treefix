# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
setattr(self, name, value)
if (isinstance(value, base.Trackable) and
    not isinstance(value, def_function.Function)):
    self._track_trackable(value, name)
