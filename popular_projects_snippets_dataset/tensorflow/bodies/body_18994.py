# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
if x.dtype == dtypes.bool:
    exit(gen_math_ops.logical_not(x, name=name))
exit(gen_bitwise_ops.invert(x, name=name))
