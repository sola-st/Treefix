# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
# These cannot be done in the automated (base test class) tests since they
# test shapes that tf.batch_matmul cannot handle.
# In particular, tf.batch_matmul does not broadcast.
with self.cached_session() as sess:
    # Given this x and LinearOperatorScaledIdentity shape of (3, 3), the
    # broadcast shape of operator and 'x' is (1, 2, 3, 4), which is the same
    # shape as x.
    x = random_ops.random_normal(shape=(1, 2, 3, 4))

    # operator is 2.2 * identity (with a batch shape).
    operator = linalg_lib.LinearOperatorScaledIdentity(
        num_rows=3, multiplier=2.2)

    # Test matmul
    expected = x * 2.2
    operator_matmul = operator.matmul(x)
    self.assertAllEqual(operator_matmul.shape, expected.shape)
    self.assertAllClose(*self.evaluate([operator_matmul, expected]))

    # Test solve
    expected = x / 2.2
    operator_solve = operator.solve(x)
    self.assertAllEqual(operator_solve.shape, expected.shape)
    self.assertAllClose(*self.evaluate([operator_solve, expected]))
