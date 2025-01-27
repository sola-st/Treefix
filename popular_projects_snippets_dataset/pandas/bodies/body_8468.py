# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_unique.py
dups = rand_series_with_duplicate_datetimeindex
index = dups.index

uniques = index.unique()
expected = DatetimeIndex(
    [
        datetime(2000, 1, 2),
        datetime(2000, 1, 3),
        datetime(2000, 1, 4),
        datetime(2000, 1, 5),
    ]
)
assert uniques.dtype == "M8[ns]"  # sanity
tm.assert_index_equal(uniques, expected)
assert index.nunique() == 4

# GH#2563
assert isinstance(uniques, DatetimeIndex)

dups_local = index.tz_localize("US/Eastern")
dups_local.name = "foo"
result = dups_local.unique()
expected = DatetimeIndex(expected, name="foo")
expected = expected.tz_localize("US/Eastern")
assert result.tz is not None
assert result.name == "foo"
tm.assert_index_equal(result, expected)
