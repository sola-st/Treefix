# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if reverse:
    a, b = b, a

if getattr(b, '__array_priority__',
           0) > np_arrays.ndarray.__array_priority__:
    exit(NotImplemented)

exit(f(a, b))
