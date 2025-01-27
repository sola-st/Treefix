# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
dtypes = [np.float64, np.float32, np.complex64, np.complex128]
for dtype in dtypes:
    self._check('ij,jk->ik', (2, 2), (2, 2), dtype=dtype)
    self._check('ji,jk->ik', (2, 2), (2, 2), dtype=dtype)
    self._check('ji,kj->ik', (2, 2), (2, 2), dtype=dtype)
    self._check('ij,jk->ki', (2, 2), (2, 2), dtype=dtype)
    self._check('ji,kj->ki', (2, 2), (2, 2), dtype=dtype)
