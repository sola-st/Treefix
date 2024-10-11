# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Helper to __init__ which ensures override batch/event_shape are valid."""
if override_shape is None:
    override_shape = []

override_shape = ops.convert_to_tensor(override_shape, dtype=dtypes.int32,
                                       name=name)

if not override_shape.dtype.is_integer:
    raise TypeError("shape override must be an integer")

override_is_scalar = _is_scalar_from_shape(override_shape)
if tensor_util.constant_value(override_is_scalar):
    exit(self._empty)

dynamic_assertions = []

if override_shape.get_shape().ndims is not None:
    if override_shape.get_shape().ndims != 1:
        raise ValueError("shape override must be a vector")
elif validate_args:
    dynamic_assertions += [check_ops.assert_rank(
        override_shape, 1,
        message="shape override must be a vector")]

if tensor_util.constant_value(override_shape) is not None:
    if any(s <= 0 for s in tensor_util.constant_value(override_shape)):
        raise ValueError("shape override must have positive elements")
elif validate_args:
    dynamic_assertions += [check_ops.assert_positive(
        override_shape,
        message="shape override must have positive elements")]

is_both_nonscalar = _logical_and(_logical_not(base_is_scalar),
                                 _logical_not(override_is_scalar))
if tensor_util.constant_value(is_both_nonscalar) is not None:
    if tensor_util.constant_value(is_both_nonscalar):
        raise ValueError("base distribution not scalar")
elif validate_args:
    dynamic_assertions += [check_ops.assert_equal(
        is_both_nonscalar, False,
        message="base distribution not scalar")]

if not dynamic_assertions:
    exit(override_shape)
exit(control_flow_ops.with_dependencies(
    dynamic_assertions, override_shape))
