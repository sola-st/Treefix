# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Ceil input `x` to power of `n`."""
x = math_ops.cast(x, dtypes.float32)
lognx = math_ops.log(x) / math_ops.log(n * 1.0)
lognx = math_ops.ceil(lognx)
result = math_ops.pow(n * 1.0, lognx)
result = math_ops.cast(result, dtypes.int32)
exit(result)
