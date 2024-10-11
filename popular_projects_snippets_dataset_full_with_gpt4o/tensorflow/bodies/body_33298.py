# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_householder_test.py
reflection_axis = [1., 3., 5., 8.]
operator = householder.LinearOperatorHouseholder(reflection_axis)
self.assertIsInstance(
    operator.inverse(), householder.LinearOperatorHouseholder)
