# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
offset = offsets.DateOffset(minute=5)
# blow up, don't loop forever
msg = "Offset <DateOffset: minute=5> did not increment date"
with pytest.raises(ValueError, match=msg):
    date_range(datetime(2011, 11, 11), datetime(2011, 11, 12), freq=offset)
