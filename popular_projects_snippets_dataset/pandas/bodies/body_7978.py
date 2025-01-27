# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
raw = [2005, 2007, 2009]
index = PeriodIndex(raw, freq="A")

expected = Index([str(num) for num in raw])
res = index.map(str)

# should return an Index
assert isinstance(res, Index)

# preserve element types
assert all(isinstance(resi, str) for resi in res)

# lastly, values should compare equal
tm.assert_index_equal(res, expected)
