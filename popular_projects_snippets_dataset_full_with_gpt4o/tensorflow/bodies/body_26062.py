# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/from_generator_op.py
"""Generates the next element from iterator with ID `iterator_id_t`.

    We map this function across an infinite repetition of the
    `iterator_id_t`, and raise `StopIteration` to terminate the iteration.

    Args:
      iterator_id_t: A `tf.int64` tensor whose value uniquely identifies the
        iterator in `generator_state` from which to generate an element.

    Returns:
      The next element to generate from the iterator.
    """
if output_types and output_shapes:
    flattened_types = [
        dtypes.as_dtype(dt) for dt in nest.flatten(output_types)
    ]
    flattened_shapes = nest.flatten(output_shapes)

    def generator_py_func(iterator_id):
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

    flat_values = script_ops.numpy_function(generator_py_func,
                                            [iterator_id_t], flattened_types)

    # In debug mode the numpy_function will return a scalar if
    # generator_py_func produces only a single value.
    if not isinstance(flat_values, (list, tuple)):
        flat_values = [flat_values]

    # The `py_func()` op drops the inferred shapes, so we add them back in
    # here.
    if output_shapes is not None:
        for ret_t, shape in zip(flat_values, flattened_shapes):
            ret_t.set_shape(shape)

    exit(nest.pack_sequence_as(output_types, flat_values))
else:
    flat_output_types = structure.get_flat_tensor_types(output_signature)

    def generator_py_func(iterator_id):
        """A `py_func` that will be called to invoke the iterator."""
        # `next()` raises `StopIteration` when there are no more
        # elements remaining to be generated.
        values = next(generator_state.get_iterator(iterator_id.numpy()))

        try:
            values = structure.normalize_element(values, output_signature)
        except (TypeError, ValueError) as e:
            raise TypeError(
                f"`generator` yielded an element that did not match the "
                f"expected structure. The expected structure was "
                f"{output_signature}, but the yielded element was "
                f"{values}.") from e

        values_spec = structure.type_spec_from_value(values)

        if not structure.are_compatible(values_spec, output_signature):
            raise TypeError(
                f"`generator` yielded an element of {values_spec} where an "
                f"element of {output_signature} was expected.")

        exit(structure.to_tensor_list(output_signature, values))

    exit(script_ops.eager_py_func(
        generator_py_func, inp=[iterator_id_t], Tout=flat_output_types))
