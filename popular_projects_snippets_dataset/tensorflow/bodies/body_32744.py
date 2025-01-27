# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
if test.is_built_with_rocm():
    self.skipTest('Incorrect Regex on rocm')
if not test.is_gpu_available():
    self.skipTest('Test requires GPU')
self._testErrorWithShapesEager('Input must have rank >= 2, but got ',
                               [2], [2], [2], [2])
self._testErrorWithShapesEager(
    'superdiag must have same rank as rhs, but got 3 and 2',
    [2, 1, 2], [2, 1], [2, 1], [2, 2])
self._testErrorWithShapesEager(
    'maindiag must have same outer dimensions as rhs, but for index 0, got '
    '3 and 2',
    [2, 1, 2], [3, 1, 2], [2, 1, 2], [2, 2, 2])
self._testErrorWithShapesEager(
    "subdiag's second-to-last dimension must be 1, but got 3",
    [2, 1, 2], [2, 1, 2], [2, 3, 2], [2, 2, 2])
self._testErrorWithShapesEager(
    "subdiag's last dimension size must be rhs's second-to-last dimension "
    "size, but got 3 and 2",
    [2, 1, 2], [2, 1, 2], [2, 1, 3], [2, 2, 2])
