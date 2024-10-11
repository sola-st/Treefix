# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
df = DataFrame(
    {"A": [1, 2, 3]},
    index=[datetime(2011, 11, 1), datetime(2011, 11, 2), datetime(2011, 11, 3)],
)
df = df.asfreq("B")
assert isinstance(df.index, DatetimeIndex)

ts = df["A"].asfreq("B")
assert isinstance(ts.index, DatetimeIndex)
