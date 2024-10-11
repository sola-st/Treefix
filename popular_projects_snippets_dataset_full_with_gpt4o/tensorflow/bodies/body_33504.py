# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
# These cannot be done in the automated (base test class) tests since they
# test shapes that tf.batch_matmul cannot handle.
# In particular, tf.batch_matmul does not broadcast.
with self.cached_session():
    x = array_ops.placeholder_with_default(rng.randn(1, 2, 3, 4), shape=None)
    operator = linalg_lib.LinearOperatorIdentity(num_rows=3, dtype=x.dtype)

    operator_matmul = operator.matmul(x)
    expected = x

    self.assertAllClose(*self.evaluate([operator_matmul, expected]))
