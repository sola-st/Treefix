# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_matmul_ops_test.py
with self.test_scope():
    shape = [77, 10, 3, 5, 7]
    superdiag = random.stateless_random_uniform(
        shape=shape[:-1], dtype=dtypes.float32, seed=[5, 10])
    maindiag = random.stateless_random_uniform(
        shape=shape[:-1], dtype=dtypes.float32, seed=[5, 11])
    subdiag = random.stateless_random_uniform(
        shape=shape[:-1], dtype=dtypes.float32, seed=[5, 12])
    rhs = random.stateless_random_uniform(
        shape=shape, dtype=dtypes.float32, seed=[5, 13])

    expected = self._tridiagonal_matmul((superdiag, maindiag, subdiag),
                                        rhs,
                                        diagonals_format='sequence')

    real = self._jit_tridiagonal_matmul((superdiag, maindiag, subdiag),
                                        rhs,
                                        diagonals_format='sequence')

    self.assertAllClose(expected, real)
