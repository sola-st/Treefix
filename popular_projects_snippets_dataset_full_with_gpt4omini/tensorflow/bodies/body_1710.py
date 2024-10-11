# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
for dtype in self._supported_key_types():
    x = self._shuffled_arange((101,), dtype)
    self._assertOpOutputMatchesExpected(
        xla.sort, [x], expected=[np.arange(101, dtype=dtype)])
