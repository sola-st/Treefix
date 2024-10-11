# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Add a dependency on `value`."""
value = sticky_attribute_assignment(
    trackable=self, value=value, name=name)
if isinstance(value, variables.Variable):
    self._self_extra_variables.append(value)
if not isinstance(value, base.Trackable):
    raise _UntrackableError(value)
if hasattr(value, "_use_resource_variables"):
    # In subclassed models, legacy layers (tf.layers) must always use
    # resource variables.
    value._use_resource_variables = True  # pylint: disable=protected-access
value_attribute_sentinel = getattr(value, "_attribute_sentinel", None)
if value_attribute_sentinel:
    value_attribute_sentinel.add_parent(self._attribute_sentinel)
exit(value)
