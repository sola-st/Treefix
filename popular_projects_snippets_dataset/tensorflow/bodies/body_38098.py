# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
# We don't use any numbers >= 10 so that lexicographical order agrees with
# numeric order in this test, for the type dtype == tf.string.

# [3 7 5 3 1]
# [2 6 5 4]
# []
# [9 8]
sp_a = sparse_tensor_lib.SparseTensor(
    indices=constant_op.constant(
        [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2],
         [1, 3], [3, 0], [3, 1]],
        dtype=dtypes.int64),
    values=_constant([3, 7, 5, 3, 1, 2, 6, 5, 4, 9, 8], dtype),
    dense_shape=constant_op.constant([4, 5], dtype=dtypes.int64))

# [9 7]
# [5 2 0]
# [6]
# []
sp_b = sparse_tensor_lib.SparseTensor(
    indices=constant_op.constant(
        [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 0]],
        dtype=dtypes.int64),
    values=_constant([9, 7, 5, 2, 0, 6], dtype),
    dense_shape=constant_op.constant([4, 3], dtype=dtypes.int64))
# The union should be
# [1 3 5 7 9]
# [0 2 4 5 6]
# [6]
# [8 9]
result = sets.set_union(sp_a, sp_b)
self.assertAllEqual(result.dense_shape, [4, 5])
self.assertAllEqual(result.indices,
                    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1],
                     [1, 2], [1, 3], [1, 4], [2, 0], [3, 0], [3, 1]])
self.assertAllEqual(
    result.values,
    _constant([1, 3, 5, 7, 9, 0, 2, 4, 5, 6, 6, 8, 9], dtype))
