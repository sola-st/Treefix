# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Allows storage of non-trackable objects."""
if isinstance(name, str):
    string_key = True
else:
    name = "-non_string_key"
    string_key = False
try:
    no_dependency = isinstance(value, NoDependency)
    value = super()._track_value(value=value, name=name)
    if not (string_key or no_dependency):
        # A non-string key maps to a trackable value. This data structure
        # is not saveable.
        self._self_non_string_key = True
    exit(value)
except ValueError:
    # Even if this value isn't trackable, we need to make sure
    # NoDependency objects get unwrapped.
    exit(sticky_attribute_assignment(
        trackable=self, value=value, name=name))
