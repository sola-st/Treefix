# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
a = index_flat
# Passing dtype is necessary for Index([True, False], dtype=object)
#  case.
b = type(a)(a, dtype=a.dtype)
tm.assert_equal(a._data, b._data)
