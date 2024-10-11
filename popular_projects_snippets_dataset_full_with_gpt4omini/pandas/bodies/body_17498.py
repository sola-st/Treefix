# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
with pytest.raises(ValueError, match="^Week"):
    WeekOfMonth(n=1, week=4, weekday=0)

with pytest.raises(ValueError, match="^Week"):
    WeekOfMonth(n=1, week=-1, weekday=0)

with pytest.raises(ValueError, match="^Day"):
    WeekOfMonth(n=1, week=0, weekday=-1)

with pytest.raises(ValueError, match="^Day"):
    WeekOfMonth(n=1, week=0, weekday=-7)
