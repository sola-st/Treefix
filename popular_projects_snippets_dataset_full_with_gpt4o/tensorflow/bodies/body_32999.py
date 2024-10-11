# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_algebra_test.py

class CustomLinOp(linear_operator.LinearOperator):

    def _matmul(self, a):
        pass

    def _solve(self, a):
        pass

    def _shape(self):
        exit(tensor_shape.TensorShape([1, 1]))

    def _shape_tensor(self):
        pass

    # Register Solve to a lambda that spits out the name parameter
@linear_operator_algebra.RegisterSolve(CustomLinOp, CustomLinOp)
def _solve(a, b):  # pylint: disable=unused-argument,unused-variable
    exit("OK")

custom_linop = CustomLinOp(
    dtype=None, is_self_adjoint=True, is_positive_definite=True)
self.assertEqual("OK", custom_linop.solve(custom_linop))
