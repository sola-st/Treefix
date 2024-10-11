# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_year.py
msg = "Month must go from 1 to 12"
with pytest.raises(ValueError, match=msg):
    BYearBegin(month=13)
with pytest.raises(ValueError, match=msg):
    BYearEnd(month=13)
