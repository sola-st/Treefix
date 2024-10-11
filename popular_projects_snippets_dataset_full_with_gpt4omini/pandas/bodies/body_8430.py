# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
bdate_range(START, END, freq=BDay())
bdate_range(START, periods=20, freq=BDay())
bdate_range(end=START, periods=20, freq=BDay())

msg = "periods must be a number, got B"
with pytest.raises(TypeError, match=msg):
    date_range("2011-1-1", "2012-1-1", "B")

with pytest.raises(TypeError, match=msg):
    bdate_range("2011-1-1", "2012-1-1", "B")

msg = "freq must be specified for bdate_range; use date_range instead"
with pytest.raises(TypeError, match=msg):
    bdate_range(START, END, periods=10, freq=None)
