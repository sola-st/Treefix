# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
# x.batch_shape =    [1, 2]
# y.batch_shape = [1, 3, 1]
# broadcast batch shape = [1, 3, 2]
x = rng.rand(1, 2, 1, 5)
y = rng.rand(1, 3, 2, 3, 7)
batch_of_zeros = np.zeros((1, 3, 2, 1, 1))
x_bc_expected = x + batch_of_zeros
y_bc_expected = y + batch_of_zeros

x_bc, y_bc = linear_operator_util.broadcast_matrix_batch_dims([x, y])

self.assertAllEqual(x_bc_expected.shape, x_bc.shape)
self.assertAllEqual(y_bc_expected.shape, y_bc.shape)
x_bc_, y_bc_ = self.evaluate([x_bc, y_bc])
self.assertAllClose(x_bc_expected, x_bc_)
self.assertAllClose(y_bc_expected, y_bc_)
