# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/qr_op_test.py
x_np = self._random_matrix(np.float32, (2000, 2000))
self._test(x_np, full_matrices=True)
