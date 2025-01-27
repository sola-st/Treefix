# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH 35690
tz = tz_aware_fixture
index = bdate_range("2000-01-03", "2000-02-11").tz_localize(tz)
key = box(year=year, month=1, day=7)

if tz is not None:
    with pytest.raises(TypeError, match="Cannot compare tz-naive"):
        # GH#36148 we require tzawareness-compat as of 2.0
        index.get_slice_bound(key, side=side)
else:
    result = index.get_slice_bound(key, side=side)
    assert result == expected
