# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
n = 2
index = func(n)
name = type(index).__name__
df = DataFrame({"a": np.random.randn(n)}, index=index)

msg = (
    "Only valid with DatetimeIndex, TimedeltaIndex "
    f"or PeriodIndex, but got an instance of '{name}'"
)
with pytest.raises(TypeError, match=msg):
    df.groupby(Grouper(freq="D"))
