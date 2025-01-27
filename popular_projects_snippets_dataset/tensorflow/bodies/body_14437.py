# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def f(x):
    if x.dtype == dtypes.bool:
        exit(array_ops.fill(array_ops.shape(x), False))
    exit(x < 0)

exit(_scalar(f, x))
