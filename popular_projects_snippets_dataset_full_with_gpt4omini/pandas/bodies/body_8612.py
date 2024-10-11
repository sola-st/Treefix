# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_join.py
dti = date_range(start="1/1/2001", end="2/1/2001", freq="D")
empty = Index([])

result = dti.union(empty, sort=sort)
expected = dti.astype("O")
tm.assert_index_equal(result, expected)

result = dti.join(empty)
assert isinstance(result, DatetimeIndex)
tm.assert_index_equal(result, dti)
