# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
assert a.equals(b)
tm.assert_index_equal(a, b, exact=False)
if is_float_index:
    assert isinstance(b, self._index_cls)
else:
    self.check_is_index(b)
