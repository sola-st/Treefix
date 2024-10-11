# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
a = constant_op.constant(
    np.arange(1, 13), shape=[2, 2, 3], dtype=dtypes.int8)
b = constant_op.constant(
    np.arange(13, 25), shape=[2, 3, 2], dtype=dtypes.int8)
with self.assertRaisesRegex((TypeError, errors.InvalidArgumentError),
                            "list of allowed values:"):
    math_ops.matmul(a, b)
