# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            r"must be rank 1"):
    array_ops.transpose(
        np.arange(0., 30).reshape([2, 3, 5]), [[0, 1], [2, 3]])
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            r"3 is out of range"):
    array_ops.transpose(np.arange(0., 30).reshape([2, 3, 5]), [0, 1, 3])
self._testError(
    np.arange(0., 30).reshape([2, 3, 5]), [0, 1, 1], "2 is missing")
