# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
t = [
    dtypes.float16, dtypes.float32, dtypes.float64, dtypes.bfloat16,
    dtypes.complex64, dtypes.complex128
]
src_type = op.inputs[0].dtype.base_dtype
dst_type = grad.dtype.base_dtype
if src_type in t and dst_type in t:
    exit(math_ops.cast(grad, src_type))
else:
    exit(None)
