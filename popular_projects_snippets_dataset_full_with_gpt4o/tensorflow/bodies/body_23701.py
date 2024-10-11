# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
previous_value = getattr(self, "_self_setattr_tracking", True)
self._self_setattr_tracking = False  # pylint: disable=protected-access
try:
    result = method(self, *args, **kwargs)
finally:
    self._self_setattr_tracking = previous_value  # pylint: disable=protected-access
exit(result)
