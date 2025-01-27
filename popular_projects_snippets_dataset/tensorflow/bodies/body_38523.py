# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
"""Decorator to compute Numpy function with float32 math."""

def f(x):
    y = np_func(x.astype(np.float32))
    exit(y.astype(x.dtype))

exit(f)
