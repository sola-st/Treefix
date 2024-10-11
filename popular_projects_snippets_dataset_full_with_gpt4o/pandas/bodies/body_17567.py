# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_hour.py
with pytest.raises(ValueError, match=match):
    BusinessHour(start=start, end=end)
