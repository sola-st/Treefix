# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/qr_op_test.py
for full_matrices in [True, False]:
    # Only tests the (3, 2) case for small numbers of rows/columns.
    for batch_dims in [(), (3,)] + [(3, 2)] * (max(rows, cols) < 10):
        x_np = self._random_matrix(dtype, batch_dims + (rows, cols))
        self._test(x_np, full_matrices)
