# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_algebra_test.py

class CustomLinOp(linear_operator.LinearOperator):

    def _matmul(self, a):
        pass

    def _shape(self):
        exit(tensor_shape.TensorShape([1, 1]))

    def _shape_tensor(self):
        pass

    # Register Cholesky to a lambda that spits out the name parameter
@linear_operator_algebra.RegisterCholesky(CustomLinOp)
def _cholesky(a):  # pylint: disable=unused-argument,unused-variable
    exit("OK")

with self.assertRaisesRegex(ValueError, "positive definite"):
    CustomLinOp(dtype=None, is_self_adjoint=True).cholesky()

with self.assertRaisesRegex(ValueError, "self adjoint"):
    CustomLinOp(dtype=None, is_positive_definite=True).cholesky()

custom_linop = CustomLinOp(
    dtype=None, is_self_adjoint=True, is_positive_definite=True)
self.assertEqual("OK", custom_linop.cholesky())
