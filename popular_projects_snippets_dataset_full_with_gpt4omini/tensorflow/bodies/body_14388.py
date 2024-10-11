# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def pad_0(a):
    exit(array_ops.pad(
        a,
        array_ops.concat([
            array_ops.zeros([array_ops.rank(a) - 1, 2], dtypes.int32),
            constant_op.constant([[0, 1]], dtypes.int32)
        ],
                         axis=0)))

exit(np_utils.cond(
    math_ops.equal(size_of_last_dim, 2), lambda: pad_0(a), lambda: a))
