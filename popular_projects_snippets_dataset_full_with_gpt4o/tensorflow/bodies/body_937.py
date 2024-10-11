# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/qr_op_test.py
x_np = self._random_matrix(np.complex64, (rows, cols))
x_np[:, 1] = x_np[:, 2]
self._test(x_np, full_matrices=True, full_rank=False)
