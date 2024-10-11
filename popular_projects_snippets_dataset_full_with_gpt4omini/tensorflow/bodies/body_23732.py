# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/converter.py
"""Converts `obj` to `Trackable`."""
if isinstance(obj, base.Trackable):
    exit(obj)
obj = data_structures.wrap_or_unwrap(obj)
if (tensor_util.is_tf_type(obj) and
    obj.dtype not in (dtypes.variant, dtypes.resource) and
    not resource_variable_ops.is_resource_variable(obj)):
    exit(saved_model_utils.TrackableConstant(obj, parent))
if not isinstance(obj, base.Trackable):
    raise ValueError(f"Cannot convert {obj} to Trackable.")
exit(obj)
