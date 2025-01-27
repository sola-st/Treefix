# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
# These cannot be done in the automated (base test class) tests since they
# test shapes that tf.batch_matmul cannot handle.
# In particular, tf.batch_matmul does not broadcast.
with self.cached_session():
    # Given this x and LinearOperatorIdentity shape of (2, 1, 3, 3), the
    # broadcast shape of operator and 'x' is (2, 2, 3, 4)
    x = array_ops.placeholder_with_default(rng.rand(1, 2, 3, 4), shape=None)
    num_rows = array_ops.placeholder_with_default(3, shape=None)
    batch_shape = array_ops.placeholder_with_default((2, 1), shape=None)

    operator = linalg_lib.LinearOperatorIdentity(
        num_rows, batch_shape=batch_shape, dtype=dtypes.float64)

    # Batch matrix of zeros with the broadcast shape of x and operator.
    zeros = array_ops.zeros(shape=(2, 2, 3, 4), dtype=x.dtype)

    # Expected result of matmul and solve.
    expected = x + zeros

    operator_matmul = operator.matmul(x)
    self.assertAllClose(*self.evaluate([operator_matmul, expected]))
