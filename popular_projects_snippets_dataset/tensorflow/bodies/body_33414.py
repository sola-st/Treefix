# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = ops.convert_to_tensor(rng.rand(2, 3, 4))
operator = DomainDimensionStubOperator(3)
# Should not raise
self.evaluate(
    linear_operator_util.assert_compatible_matrix_dimensions(operator, x))
