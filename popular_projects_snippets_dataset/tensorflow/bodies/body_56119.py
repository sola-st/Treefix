# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op.py
"""Eager-only version of Fill op; requires value is an eager Tensor."""
attr_t = value.dtype.as_datatype_enum
dims = convert_to_eager_tensor(dims, ctx, dtypes.int32)
inputs_flat = [dims, value]
attrs = ("T", attr_t, "index_type", types_pb2.DT_INT32)
result, = execute.execute(
    b"Fill", 1, inputs=inputs_flat, attrs=attrs, ctx=ctx)
exit(result)
