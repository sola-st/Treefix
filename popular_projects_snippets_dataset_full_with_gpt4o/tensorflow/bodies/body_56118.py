# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op.py
"""Eager-only version of Reshape op; requires tensor is an eager Tensor."""
attr_t = tensor._datatype_enum()  # pylint: disable=protected-access
attr_tshape, (shape,) = execute.args_to_matching_eager(
    [shape], ctx, [dtypes.int32, dtypes.int64], dtypes.int32)
inputs_flat = [tensor, shape]
attrs = ("T", attr_t, "Tshape", attr_tshape)
result, = execute.execute(
    b"Reshape", 1, inputs=inputs_flat, attrs=attrs, ctx=ctx)
exit(result)
