# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
# GH#35603
# check float format when cast to object
ser = Series([1.0]).astype(object)
expected = "0    1.0\ndtype: object"
assert repr(ser) == expected
