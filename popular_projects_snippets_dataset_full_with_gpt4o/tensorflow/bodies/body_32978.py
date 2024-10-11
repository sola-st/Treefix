# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_algebra_test.py

class CustomLinOp(linear_operator.LinearOperator):
    pass

with self.assertRaisesRegex(TypeError, "must be callable"):
    linear_operator_algebra.RegisterAdjoint(CustomLinOp)("blah")

# First registration is OK
linear_operator_algebra.RegisterAdjoint(CustomLinOp)(lambda a: None)

# Second registration fails
with self.assertRaisesRegex(ValueError, "has already been registered"):
    linear_operator_algebra.RegisterAdjoint(CustomLinOp)(lambda a: None)
