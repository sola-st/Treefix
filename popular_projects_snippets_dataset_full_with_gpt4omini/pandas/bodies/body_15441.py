# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
dtype = obj.dtype if is_inplace else object
expected = Series([val] + list(obj[1:]), dtype=dtype)
exit(expected)
