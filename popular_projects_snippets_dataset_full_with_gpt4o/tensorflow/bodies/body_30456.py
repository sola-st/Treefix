# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
for t in [np.complex64, np.complex128]:
    x = np.random.rand(2, 5).astype(t)
    self._testAll(x + 1j * x, [[1, 0], [2, 0]], 1234.0 - 1234.0j)
    x = np.random.rand(3, 2, 1, 1).astype(t)
    self._testAll(x + 1j * x, [[0, 0], [0, 0], [0, 0], [0, 0]], 0 + 0j)
