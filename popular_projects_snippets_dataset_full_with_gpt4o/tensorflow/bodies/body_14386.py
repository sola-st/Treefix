# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def move_axis_to_last(a, axis):
    exit(array_ops.transpose(
        a,
        array_ops.concat([
            math_ops.range(axis),
            math_ops.range(axis + 1, array_ops.rank(a)), [axis]
        ],
                         axis=0)))

exit(np_utils.cond(axis == np_utils.subtract(array_ops.rank(a), 1),
                     lambda: a, lambda: move_axis_to_last(a, axis)))
