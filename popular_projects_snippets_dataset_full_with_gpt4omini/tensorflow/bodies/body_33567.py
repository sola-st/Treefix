# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_addition_test.py
op1 = linalg.LinearOperatorFullMatrix(rng.rand(2, 3))
op2 = linalg.LinearOperatorDiag(rng.rand(2, 4))
with self.assertRaisesRegex(ValueError, "must.*same `domain_dimension`"):
    add_operators([op1, op2])
