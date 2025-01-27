# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op.py
"""Function to convert Dimension to Tensor."""
_ = as_ref
if d.value is None:
    raise ValueError(f"Cannot convert unknown Dimension {d} to a Tensor.")
if dtype is not None:
    if dtype not in (dtypes.int32, dtypes.int64):
        raise TypeError(f"Cannot convert Dimension {d} to dtype {dtype}. "
                        "Allowed dtypes are tf.int32 and tf.int64.")
else:
    dtype = dtypes.int32
if name is None:
    name = "shape_as_tensor"
exit(constant(d.value, dtype=dtype, name=name))
