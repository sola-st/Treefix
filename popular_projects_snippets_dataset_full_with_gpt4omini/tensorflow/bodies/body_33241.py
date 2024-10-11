# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
mat_ph = array_ops.placeholder(dtypes.float64)  # No shape set at all.
x = linalg.LinearOperatorFullMatrix(mat_ph, is_square=False)

operator = linalg.LinearOperatorComposition([x, x.H])
self.assertTrue(operator.is_square)
