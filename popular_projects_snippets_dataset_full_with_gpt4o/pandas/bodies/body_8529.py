# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH 34077
tz = tz_aware_fixture
index = DatetimeIndex(["2010-01-01", "2010-01-03"]).tz_localize(tz)
key = box(2010, 1, 1)

if tz is not None:
    with pytest.raises(TypeError, match="Cannot compare tz-naive"):
        # GH#36148 we require tzawareness-compat as of 2.0
        index.slice_locs(key, box(2010, 1, 2))
else:
    result = index.slice_locs(key, box(2010, 1, 2))
    expected = (0, 1)
    assert result == expected
