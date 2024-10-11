# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
# float16 cannot be tested by base test class because tf.linalg.solve does
# not work with float16.
with self.cached_session():
    operator = linalg_lib.LinearOperatorIdentity(
        num_rows=2, dtype=dtypes.float16)
    x = rng.randn(2, 3).astype(np.float16)
    y = operator.matmul(x)
    self.assertAllClose(x, self.evaluate(y))
