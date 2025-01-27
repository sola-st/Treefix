# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_kronecker_test.py
operators = [
    linalg.LinearOperatorFullMatrix(rng.rand(2, 3, 3)),
    linalg.LinearOperatorFullMatrix(rng.rand(2, 3, 3).astype(np.float32))
]
with self.assertRaisesRegex(TypeError, "same dtype"):
    kronecker.LinearOperatorKronecker(operators)
