# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
reduction_axes = [[1], [2]]
c_unknown = array_ops.placeholder(dtypes.float32)
with self.assertRaisesWithPredicateMatch(ValueError,
                                         ".*must be at most rank 1.*"):
    math_ops.reduce_sum(c_unknown, reduction_axes)
