# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
expected = Series([scalar, scalar, 3], dtype=object)
assert isinstance(expected[0], type(scalar))
exit(expected)
