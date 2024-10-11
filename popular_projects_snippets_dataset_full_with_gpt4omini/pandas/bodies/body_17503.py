# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
with pytest.raises(ValueError, match="^N cannot be 0"):
    LastWeekOfMonth(n=0, weekday=1)

with pytest.raises(ValueError, match="^Day"):
    LastWeekOfMonth(n=1, weekday=-1)

with pytest.raises(ValueError, match="^Day"):
    LastWeekOfMonth(n=1, weekday=7)
