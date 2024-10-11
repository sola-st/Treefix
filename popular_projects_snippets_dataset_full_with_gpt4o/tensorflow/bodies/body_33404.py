# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
# x.batch_shape = [3, 1, 2]
# y.batch_shape = [4, 1]
# broadcast batch shape = [3, 4, 2]
x = rng.rand(3, 1, 2, 1, 5).astype(np.float32)
y = rng.rand(4, 1, 3, 7).astype(np.float32)
batch_of_zeros = np.zeros((3, 4, 2, 1, 1)).astype(np.float32)
x_bc_expected = x + batch_of_zeros
y_bc_expected = y + batch_of_zeros

x_ph = array_ops.placeholder_with_default(x, shape=None)
y_ph = array_ops.placeholder_with_default(y, shape=None)

x_bc, y_bc = linear_operator_util.broadcast_matrix_batch_dims([x_ph, y_ph])

x_bc_, y_bc_ = self.evaluate([x_bc, y_bc])
self.assertAllClose(x_bc_expected, x_bc_)
self.assertAllClose(y_bc_expected, y_bc_)
