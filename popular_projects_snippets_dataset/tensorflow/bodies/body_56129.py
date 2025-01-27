# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op.py
"""Function to convert TensorShape to Tensor."""
_ = as_ref
if not s.is_fully_defined():
    raise ValueError(
        f"Cannot convert a partially known TensorShape {s} to a Tensor.")
s_list = s.as_list()
int64_value = 0
for dim in s_list:
    if dim >= 2**31:
        int64_value = dim
        break

if dtype is not None:
    if dtype not in (dtypes.int32, dtypes.int64):
        raise TypeError(f"Cannot convert TensorShape {s} to dtype {dtype}. "
                        "Allowed dtypes are tf.int32 and tf.int64.")
    if dtype == dtypes.int32 and int64_value:
        raise ValueError(f"Cannot convert TensorShape {s} to dtype int32; "
                         f"a dimension is too large. Consider using tf.int64.")
else:
    dtype = dtypes.int64 if int64_value else dtypes.int32
if name is None:
    name = "shape_as_tensor"
exit(constant(s_list, dtype=dtype, name=name))
