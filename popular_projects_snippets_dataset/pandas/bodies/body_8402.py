# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
msg = r"Offset <0 \* MonthEnds> did not increment date"
with pytest.raises(ValueError, match=msg):
    date_range("1/1/2000", "1/1/2001", freq=MonthEnd(0))
