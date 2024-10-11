# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
r = array_ops.rank(a)
exit(array_ops.transpose(
    a,
    array_ops.concat(
        [math_ops.range(axis), [r - 1],
         math_ops.range(axis, r - 1)],
        axis=0)))
