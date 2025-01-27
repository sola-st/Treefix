# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
"""Checks that internal Variables are correctly converted to Tensors."""
self.assertIsInstance(operator, composite_tensor.CompositeTensor)
tensor_operator = composite_tensor.convert_variables_to_tensors(operator)
self.assertIs(type(operator), type(tensor_operator))
self.assertEmpty(tensor_operator.variables)
self._check_tensors_equal_variables(operator, tensor_operator)
