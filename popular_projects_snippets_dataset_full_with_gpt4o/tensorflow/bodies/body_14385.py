# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
exit(array_ops.transpose(
    a,
    array_ops.concat([
        math_ops.range(axis),
        math_ops.range(axis + 1, array_ops.rank(a)), [axis]
    ],
                     axis=0)))
