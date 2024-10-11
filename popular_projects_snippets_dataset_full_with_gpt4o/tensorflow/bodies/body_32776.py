# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py

shape = (1, 2, 3, 4)
operator = LinearOperatorShape(shape)

self.assertAllEqual(shape, operator.shape)
self.assertAllEqual(4, operator.tensor_rank)
self.assertAllEqual((1, 2), operator.batch_shape)
self.assertAllEqual(4, operator.domain_dimension)
self.assertAllEqual(3, operator.range_dimension)
expected_parameters = {
    "is_non_singular": None,
    "is_positive_definite": None,
    "is_self_adjoint": None,
    "is_square": None,
    "shape": (1, 2, 3, 4),
}
self.assertEqual(expected_parameters, operator.parameters)
