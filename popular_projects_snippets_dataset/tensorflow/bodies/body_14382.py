# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
exit(_bin_op(lambda a, b: math_ops.tensordot(a, b, axes=axes), a, b))
