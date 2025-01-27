# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# issue 18488
msg = "Start and end cannot both be tz-aware with different timezones"
with pytest.raises(TypeError, match=msg):
    date_range(start, end)
with pytest.raises(TypeError, match=msg):
    date_range(start, end, freq=BDay())
