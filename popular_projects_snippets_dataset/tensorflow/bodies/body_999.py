# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
for dtype in self.numeric_types - self.complex_types:
    self._assertOpOutputMatchesExpected(
        gen_functional_ops.to_bool,
        np.array(5, dtype=dtype),
        expected=np.array(True))

    self._assertOpOutputMatchesExpected(
        gen_functional_ops.to_bool,
        np.array(0, dtype=dtype),
        expected=np.array(False))

    self._assertOpOutputMatchesExpected(
        gen_functional_ops.to_bool,
        np.array([], dtype=dtype),
        expected=np.array(False))

    self._assertOpOutputMatchesExpected(
        gen_functional_ops.to_bool,
        np.array([1, 2, 3], dtype=dtype),
        expected=np.array(True))
