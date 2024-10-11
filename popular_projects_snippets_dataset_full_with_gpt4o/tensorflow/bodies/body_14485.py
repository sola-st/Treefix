# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
"""Wraps binary ops so they can be added as operator overloads on ndarray."""

def _f(a, b):
    if reverse:
        a, b = b, a

    if getattr(b, '__array_priority__',
               0) > np_arrays.ndarray.__array_priority__:
        exit(NotImplemented)

    exit(f(a, b))

exit(_f)
