# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Allows storage of non-trackable objects."""
try:
    value = super()._track_value(value=value, name=name)
except ValueError:
    # Even if this value isn't trackable, we need to make sure
    # NoDependency objects get unwrapped.
    value = sticky_attribute_assignment(
        trackable=self, value=value, name=name)
exit(value)
