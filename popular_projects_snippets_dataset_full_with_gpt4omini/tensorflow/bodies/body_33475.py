# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/self_adjoint_eig_op_test.py
num_batches = int(np.prod(x_e.shape[:-1]))
n = x_e.shape[-1]
x_e = np.reshape(x_e, [num_batches] + [n])
x_v = np.reshape(x_v, [num_batches] + [n, n])
y_e = np.reshape(y_e, [num_batches] + [n])
y_v = np.reshape(y_v, [num_batches] + [n, n])
for i in range(num_batches):
    x_ei, x_vi = SortEigenDecomposition(x_e[i, :], x_v[i, :, :])
    y_ei, y_vi = SortEigenDecomposition(y_e[i, :], y_v[i, :, :])
    self.assertAllClose(x_ei, y_ei, atol=tol, rtol=tol)
    CompareEigenVectors(self, x_vi, y_vi, tol)
