# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
with pytest.raises(ValueError, match="Day must be"):
    Week(weekday=7)

with pytest.raises(ValueError, match="Day must be"):
    Week(weekday=-1)
