# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/slicing_test.py
matrix = linear_operator_test_util.random_normal(
    shape=[1, 4, 3, 2, 2], dtype=dtypes.float32)
operator = linalg.LinearOperatorFullMatrix(matrix, is_square=True)
sliced = operator[..., array_ops.newaxis, 2:, array_ops.newaxis]

self.assertAllEqual(
    list(array_ops.zeros([1, 4, 3])[
        ..., array_ops.newaxis, 2:, array_ops.newaxis].shape),
    sliced.batch_shape_tensor())
