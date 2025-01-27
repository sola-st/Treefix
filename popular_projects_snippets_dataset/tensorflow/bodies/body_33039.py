# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_kronecker_test.py
x = ops.convert_to_tensor([[2., 3.], [1., 2.]], dtype=dtypes.float32)
y = ops.convert_to_tensor([[1., 2.], [5., -1.]], dtype=dtypes.float32)
# From explicitly writing out the kronecker product of x and y.
z = ops.convert_to_tensor([
    [2., 4., 3., 6.],
    [10., -2., 15., -3.],
    [1., 2., 2., 4.],
    [5., -1., 10., -2.]], dtype=dtypes.float32)
# From explicitly writing out the kronecker product of y and x.
w = ops.convert_to_tensor([
    [2., 3., 4., 6.],
    [1., 2., 2., 4.],
    [10., 15., -2., -3.],
    [5., 10., -1., -2.]], dtype=dtypes.float32)

self.assertAllClose(
    self.evaluate(_kronecker_dense([x, y])), self.evaluate(z))
self.assertAllClose(
    self.evaluate(_kronecker_dense([y, x])), self.evaluate(w))
