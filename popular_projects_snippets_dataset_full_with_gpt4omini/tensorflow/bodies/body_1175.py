# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cholesky_op_test.py
for dtype in self.float_types:
    condition_number = 1000
    size = 20

    # Generate random positive-definite symmetric matrices, and take their
    # Eigendecomposition.
    matrix = np.random.rand(size, size)
    matrix = np.dot(matrix.T, matrix)
    _, w = np.linalg.eigh(matrix)

    # Build new Eigenvalues exponentially distributed between 1 and
    # 1/condition_number
    v = np.exp(-np.log(condition_number) * np.linspace(0, size, size) / size)
    matrix = np.dot(np.dot(w, np.diag(v)), w.T).astype(dtype)
    self._verifyCholesky(matrix, atol=1e-4)
