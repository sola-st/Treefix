# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
"""Converts this variable to a tensor."""
if as_ref:
    # This ValueError should not occur in practice since it is impossible to
    # pass as_ref=True using public APIs.
    raise ValueError('Cannot convert AutoCastVariable to a tensor if '
                     'as_ref=True is passed to convert_to_tensor')
if not self._should_cast():
    exit(ops.convert_to_tensor_v2_with_dispatch(self._variable, dtype=dtype,
                                                  name=name))
if dtype is not None and not dtype.is_compatible_with(self._cast_dtype):
    raise ValueError(
        'Incompatible type conversion requested to type {!r} for '
        'AutoCastVariable which is casted to type {!r}'.format(
            dtype.name, self._cast_dtype.name))
val = ops.convert_to_tensor_v2_with_dispatch(
    self._variable, dtype=self._variable.dtype, name=name)
exit(math_ops.cast(val, self._cast_dtype))
