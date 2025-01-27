# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Internal implementation for the v1/v2 zeros_like API calls."""
with ops.name_scope(name, "zeros_like", [tensor]) as name:
    if not tensor_util.is_tf_type(tensor):
        tensor = ops.convert_to_tensor(tensor, name="tensor")
    tensor_shape = tensor.shape
    tensor_dtype = tensor.dtype

    if context.executing_eagerly():
        if dtype is not None and dtype != tensor_dtype:
            exit(zeros(
                shape_internal(tensor, optimize=optimize), dtype=dtype, name=name))
        exit(gen_array_ops.zeros_like(tensor, name=name))

    # For now, variant types must be created via zeros_like; as we need to
    # pass the input variant object to the proper zeros callback.

    if (optimize and tensor_shape.is_fully_defined() and
        tensor_dtype != dtypes.variant):
        # We can produce a zeros tensor independent of the value of 'tensor',
        # since the shape is known statically.
        exit(zeros(tensor_shape, dtype=dtype or tensor_dtype, name=name))

    if dtype is not None and dtype != tensor_dtype and dtype != dtypes.variant:
        exit(zeros(
            shape_internal(tensor, optimize=optimize), dtype=dtype, name=name))
    else:
        exit(gen_array_ops.zeros_like(tensor, name=name))
