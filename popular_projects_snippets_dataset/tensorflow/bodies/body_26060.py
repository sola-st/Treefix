# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/from_generator_op.py
"""A `py_func` that will be called to invoke the iterator."""
# `next()` raises `StopIteration` when there are no more
# elements remaining to be generated.
values = next(generator_state.get_iterator(iterator_id))

# Use the same _convert function from the py_func() implementation to
# convert the returned values to arrays early, so that we can inspect
# their values.
try:
    flattened_values = nest.flatten_up_to(output_types, values)
except (TypeError, ValueError) as e:
    raise TypeError(
        f"`generator` yielded an element that did not match the "
        f"expected structure. The expected structure was "
        f"{output_types}, but the yielded element was {values}.") from e
ret_arrays = []
for ret, dtype in zip(flattened_values, flattened_types):
    try:
        ret_arrays.append(
            script_ops.FuncRegistry._convert(  # pylint: disable=protected-access
                ret,
                dtype=dtype.as_numpy_dtype))
    except (TypeError, ValueError) as e:
        raise TypeError(
            f"`generator` yielded an element that could not be "
            f"converted to the expected type. The expected type was "
            f"{dtype.name}, but the yielded element was {ret}.") from e

        # Additional type and shape checking to ensure that the components of
        # the generated element match the `output_types` and `output_shapes`
        # arguments.
for (ret_array, expected_dtype,
     expected_shape) in zip(ret_arrays, flattened_types,
                            flattened_shapes):
    if ret_array.dtype != expected_dtype.as_numpy_dtype:
        raise TypeError(
            f"`generator` yielded an element of type {ret_array.dtype} "
            f"where an element of type {expected_dtype.as_numpy_dtype} "
            f"was expected.")
    if not expected_shape.is_compatible_with(ret_array.shape):
        raise TypeError(
            f"`generator` yielded an element of shape {ret_array.shape} "
            f"where an element of shape {expected_shape} was expected.")

exit(ret_arrays)
