# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
operator = linalg_lib.LinearOperatorIdentity(num_rows=2)
x = rng.randn(3, 3).astype(np.float32)
with self.assertRaisesRegex(ValueError, "Dimensions.*not compatible"):
    operator.matmul(x)
