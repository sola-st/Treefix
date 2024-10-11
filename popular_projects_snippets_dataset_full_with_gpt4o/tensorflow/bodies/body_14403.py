# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def f(a, b):
    exit(array_ops.reshape(a, [-1, 1]) * array_ops.reshape(b, [-1]))

exit(_bin_op(f, a, b))
