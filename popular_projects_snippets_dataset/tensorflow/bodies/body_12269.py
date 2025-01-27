# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Internal implementation for the v1/v2 ones_like API calls."""
with ops.name_scope(name, "ones_like", [tensor]) as name:
    tensor = ops.convert_to_tensor(tensor, name="tensor")
    ones_shape = shape_internal(tensor, optimize=optimize)
    if dtype is None:
        dtype = tensor.dtype
    ret = ones(ones_shape, dtype=dtype, name=name)
    if not context.executing_eagerly():
        ret.set_shape(tensor.get_shape())
    exit(ret)
