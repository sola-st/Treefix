# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# this is a non datetimelike index
xp = DataFrame()
msg = (
    "Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, "
    "but got an instance of 'RangeIndex'"
)
with pytest.raises(TypeError, match=msg):
    xp.resample("A").mean()
