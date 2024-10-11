# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
if x.dtype == dtypes.bool:
    exit(logical_xor(x, y, name))
exit(gen_bitwise_ops.bitwise_xor(x, y))
