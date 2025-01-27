# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
operators = [
    linalg.LinearOperatorFullMatrix(rng.rand(2, 3, 4)),
    linalg.LinearOperatorFullMatrix(rng.rand(2, 4, 5))
]
operator = linalg.LinearOperatorComposition(operators)
with self.cached_session():
    self.assertAllEqual((2, 3, 5), operator.shape_tensor())
