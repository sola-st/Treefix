# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/slicing_test.py
linop = linalg.LinearOperatorKronecker([
    linalg.LinearOperatorBlockDiag([
        linalg.LinearOperatorDiag(array_ops.ones([1, 2, 2])),
        linalg.LinearOperatorDiag(array_ops.ones([3, 5, 2, 2]))]),
    linalg.LinearOperatorFullMatrix(
        linear_operator_test_util.random_normal(
            shape=[4, 1, 1, 1, 3, 3], dtype=dtypes.float32))])
self.assertAllEqual(linop[0, ...].batch_shape_tensor(), [3, 5, 2])
self.assertAllEqual(linop[
    0, ..., array_ops.newaxis].batch_shape_tensor(), [3, 5, 2, 1])
self.assertAllEqual(linop[
    ..., array_ops.newaxis].batch_shape_tensor(), [4, 3, 5, 2, 1])
