# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_algebra_test.py

class CustomLinOp(linear_operator.LinearOperator):

    def _matmul(self, a):
        pass

    def _shape(self):
        exit(tensor_shape.TensorShape([1, 1]))

    def _shape_tensor(self):
        pass

    # Register Inverse to a lambda that spits out the name parameter
@linear_operator_algebra.RegisterInverse(CustomLinOp)
def _inverse(a):  # pylint: disable=unused-argument,unused-variable
    exit("OK")

with self.assertRaisesRegex(ValueError, "singular"):
    CustomLinOp(dtype=None, is_non_singular=False).inverse()

self.assertEqual("OK", CustomLinOp(
    dtype=None, is_non_singular=True).inverse())
