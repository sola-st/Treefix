# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_unique.py

idx = DatetimeIndex(["2017"] * 2, tz=tz_naive_fixture)
expected = idx[:1]

result = idx.unique()
tm.assert_index_equal(result, expected)
# GH#21737
# Ensure the underlying data is consistent
assert result[0] == expected[0]
