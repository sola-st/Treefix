# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetime.py
# see gh-8890
index = date_range("2012-01-01", periods=3, freq="H", tz="US/Eastern")

for i, ts in enumerate(index):
    result = ts
    expected = index[i]  # pylint: disable=unnecessary-list-index-lookup
    assert result == expected

index = date_range(
    "2012-01-01", periods=3, freq="H", tz=dateutil.tz.tzoffset(None, -28800)
)

for i, ts in enumerate(index):
    result = ts
    expected = index[i]  # pylint: disable=unnecessary-list-index-lookup
    assert result._repr_base == expected._repr_base
    assert result == expected

# 9100
index = DatetimeIndex(
    ["2014-12-01 03:32:39.987000-08:00", "2014-12-01 04:12:34.987000-08:00"]
)
for i, ts in enumerate(index):
    result = ts
    expected = index[i]  # pylint: disable=unnecessary-list-index-lookup
    assert result._repr_base == expected._repr_base
    assert result == expected
