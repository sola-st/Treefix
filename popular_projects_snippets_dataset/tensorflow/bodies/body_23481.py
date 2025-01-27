# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Allow any modifications, but possibly mark the wrapper as unsaveable."""
self._check_self_external_modification()
self._maybe_initialize_trackable()
no_dep = isinstance(value, NoDependency)
if isinstance(key, str):
    value = self._track_value(value, name=key)
else:
    value = wrap_or_unwrap(value)
    if not no_dep and isinstance(value, base.Trackable):
        # Non-string keys are OK as long as we have no reason to add a
        # dependency on the value (either because the value is not
        # trackable, or because it was wrapped in a NoDependency object).
        self._self_non_string_key = True
self.__wrapped__[key] = value

self._update_snapshot()
