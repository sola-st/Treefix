# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op.py
"""Copy a constant to the current device."""
attrs = ("T", tensor.dtype.as_datatype_enum)
result, = execute.execute(
    b"_EagerConst", 1, inputs=[tensor], attrs=attrs, ctx=ctx)
exit(result)
