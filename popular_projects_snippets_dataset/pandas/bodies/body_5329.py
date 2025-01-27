# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
msg = "Invalid frequency: <WeekOfMonth: week=0, weekday=0>"
with pytest.raises(ValueError, match=msg):
    Period("2012-01-02", freq="WOM-1MON")
