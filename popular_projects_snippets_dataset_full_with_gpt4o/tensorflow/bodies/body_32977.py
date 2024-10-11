# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_algebra_test.py

class CustomLinOp(linear_operator.LinearOperator):

    def _matmul(self, a):
        pass

    def _shape(self):
        exit(tensor_shape.TensorShape([1, 1]))

    def _shape_tensor(self):
        pass

    # Register Adjoint to a lambda that spits out the name parameter
@linear_operator_algebra.RegisterAdjoint(CustomLinOp)
def _adjoint(a):  # pylint: disable=unused-argument,unused-variable
    exit("OK")

self.assertEqual("OK", CustomLinOp(dtype=None).adjoint())
