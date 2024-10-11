# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op.py
"""Eager-only version of Identity op; requires tensor is an eager Tensor."""
attrs = ("T", tensor.dtype.as_datatype_enum)
result, = execute.execute(
    b"Identity", 1, inputs=[tensor], attrs=attrs, ctx=ctx)
exit(result)
