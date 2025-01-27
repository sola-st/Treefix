# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
bdate_range(START, END, freq=CDay())
bdate_range(START, periods=20, freq=CDay())
bdate_range(end=START, periods=20, freq=CDay())

msg = "periods must be a number, got C"
with pytest.raises(TypeError, match=msg):
    date_range("2011-1-1", "2012-1-1", "C")

with pytest.raises(TypeError, match=msg):
    bdate_range("2011-1-1", "2012-1-1", "C")
