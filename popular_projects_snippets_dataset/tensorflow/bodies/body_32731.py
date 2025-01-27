# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
superdiag_extended = np.pad(superdiag, [0, 1], 'constant')
subdiag_extended = np.pad(subdiag, [1, 0], 'constant')
diags_compact = np.stack([superdiag_extended, maindiag, subdiag_extended])
diags_matrix = np.diag(superdiag, 1) + np.diag(maindiag, 0) + np.diag(
    subdiag, -1)

diags_sequence = (constant_op.constant(superdiag_extended, dtype),
                  constant_op.constant(maindiag, dtype),
                  constant_op.constant(subdiag_extended, dtype))
diags_compact = constant_op.constant(diags_compact, dtype)
diags_matrix = constant_op.constant(diags_matrix, dtype)
rhs = constant_op.constant(rhs, dtype)

rhs_batch = array_ops.stack([rhs, 2 * rhs])
diags_compact_batch = array_ops.stack([diags_compact, 2 * diags_compact])
diags_matrix_batch = array_ops.stack([diags_matrix, 2 * diags_matrix])
diags_sequence_batch = [array_ops.stack([x, 2 * x]) for x in diags_sequence]

results = [
    linalg_impl.tridiagonal_matmul(
        diags_sequence, rhs, diagonals_format='sequence'),
    linalg_impl.tridiagonal_matmul(
        diags_compact, rhs, diagonals_format='compact'),
    linalg_impl.tridiagonal_matmul(
        diags_matrix, rhs, diagonals_format='matrix')
]
results_batch = [
    linalg_impl.tridiagonal_matmul(
        diags_sequence_batch, rhs_batch, diagonals_format='sequence'),
    linalg_impl.tridiagonal_matmul(
        diags_compact_batch, rhs_batch, diagonals_format='compact'),
    linalg_impl.tridiagonal_matmul(
        diags_matrix_batch, rhs_batch, diagonals_format='matrix')
]

with self.cached_session():
    results = self.evaluate(results)
    results_batch = self.evaluate(results_batch)

expected = np.array(expected)
expected_batch = np.stack([expected, 4 * expected])
for result in results:
    self.assertAllClose(result, expected)
for result in results_batch:
    self.assertAllClose(result, expected_batch)
