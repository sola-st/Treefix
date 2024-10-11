# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
op1 = linalg.LinearOperatorFullMatrix(rng.rand(2, 3))
op2 = linalg.LinearOperatorDiag(rng.rand(3, 3))
with self.assertRaisesRegex(ValueError, "must.*same `range_dimension`"):
    add_operators([op1, op2])
