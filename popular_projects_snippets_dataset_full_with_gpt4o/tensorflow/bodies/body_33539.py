# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/norm_op_test.py
matrix = [[0., 1.], [2., 3.]]
for axis_ in [], [1, 2, 3], [[1]], [[1], [2]], [3.1415], [1, 1]:
    error_prefix = ("'axis' must be None, an integer, or a tuple of 2 unique "
                    "integers")
    with self.assertRaisesRegex(ValueError, error_prefix):
        linalg_ops.norm(matrix, axis=axis_)
