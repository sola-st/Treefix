# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
badly_formed_date = "2007/100/1"

msg = "Unknown datetime string format, unable to parse: 2007/100/1"
with pytest.raises(ValueError, match=msg):
    Timestamp(badly_formed_date)

with pytest.raises(ValueError, match=msg):
    bdate_range(start=badly_formed_date, periods=10)

with pytest.raises(ValueError, match=msg):
    bdate_range(end=badly_formed_date, periods=10)

with pytest.raises(ValueError, match=msg):
    bdate_range(badly_formed_date, badly_formed_date)
