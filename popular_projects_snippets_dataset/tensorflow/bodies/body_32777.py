# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
with self.cached_session():
    shape = (1, 2, 3, 4)
    operator = LinearOperatorShape(shape)

    self.assertAllEqual(shape, self.evaluate(operator.shape_tensor()))
    self.assertAllEqual(4, self.evaluate(operator.tensor_rank_tensor()))
    self.assertAllEqual((1, 2), self.evaluate(operator.batch_shape_tensor()))
    self.assertAllEqual(4, self.evaluate(operator.domain_dimension_tensor()))
    self.assertAllEqual(3, self.evaluate(operator.range_dimension_tensor()))
