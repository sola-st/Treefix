# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
# GH 29879
ser = Series([1, 2])
comb = concat([ser, ser], axis=axis, copy=True)
assert comb.index is not ser.index
