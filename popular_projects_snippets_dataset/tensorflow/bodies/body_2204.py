# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_matmul_ops_test.py
superdiag_extended = np.pad(superdiag, [0, 1], 'constant')
subdiag_extended = np.pad(subdiag, [1, 0], 'constant')

diags_compact = np.stack([superdiag_extended, maindiag, subdiag_extended])
diags_matrix = np.diag(superdiag, 1) + np.diag(maindiag, 0) + np.diag(
    subdiag, -1)

with self.test_scope():
    diags_sequence_op = (constant_op.constant(superdiag_extended, dtype),
                         constant_op.constant(maindiag, dtype),
                         constant_op.constant(subdiag_extended, dtype))
    diags_compact_op = constant_op.constant(diags_compact, dtype)
    diags_matrix_op = constant_op.constant(diags_matrix, dtype)
    rhs_op = constant_op.constant(rhs, dtype)

    rhs_batch_op = array_ops.stack([rhs_op, 2 * rhs_op])
    diags_compact_batch_op = array_ops.stack(
        [diags_compact_op, 2 * diags_compact_op])
    diags_matrix_batch_op = array_ops.stack(
        [diags_matrix_op, 2 * diags_matrix_op])
    diags_sequence_batch_op = [
        array_ops.stack([x, 2 * x]) for x in diags_sequence_op
    ]

    results = [
        self._jit_tridiagonal_matmul(
            diags_sequence_op, rhs_op, diagonals_format='sequence'),
        self._jit_tridiagonal_matmul(
            diags_compact_op, rhs_op, diagonals_format='compact'),
        self._jit_tridiagonal_matmul(
            diags_matrix_op, rhs_op, diagonals_format='matrix')
    ]

    results_batch = [
        self._jit_tridiagonal_matmul(
            diags_sequence_batch_op,
            rhs_batch_op,
            diagonals_format='sequence'),
        self._jit_tridiagonal_matmul(
            diags_compact_batch_op, rhs_batch_op, diagonals_format='compact'),
        self._jit_tridiagonal_matmul(
            diags_matrix_batch_op, rhs_batch_op, diagonals_format='matrix')
    ]

    expected = self._tridiagonal_matmul(
        diags_sequence_op, rhs_op, diagonals_format='sequence')
    expected_batch = np.stack([expected, 4 * expected])
    for result in results:
        self.assertAllClose(result, expected)
    for result in results_batch:
        self.assertAllClose(result, expected_batch)
