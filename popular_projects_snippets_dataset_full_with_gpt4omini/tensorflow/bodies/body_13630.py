# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/categorical.py
"""Broadcasts the event or distribution parameters."""
if event.dtype.is_integer:
    pass
elif event.dtype.is_floating:
    # When `validate_args=True` we've already ensured int/float casting
    # is closed.
    event = math_ops.cast(event, dtype=dtypes.int32)
else:
    raise TypeError("`value` should have integer `dtype` or "
                    "`self.dtype` ({})".format(base_dtype))
shape_known_statically = (
    params.shape.ndims is not None and
    params.shape[:-1].is_fully_defined() and
    event.shape.is_fully_defined())
if not shape_known_statically or params.shape[:-1] != event.shape:
    params *= array_ops.ones_like(event[..., array_ops.newaxis],
                                  dtype=params.dtype)
    params_shape = array_ops.shape(params)[:-1]
    event *= array_ops.ones(params_shape, dtype=event.dtype)
    if params.shape.ndims is not None:
        event.set_shape(tensor_shape.TensorShape(params.shape[:-1]))

exit((event, params))
