# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
index = Index(
    [datetime(2000, 1, 1) + timedelta(i) for i in range(1000)], dtype=object
)
ts = Series(np.random.randn(len(index)), index)
repr(ts)

ts = tm.makeTimeSeries(1000)
assert repr(ts).splitlines()[-1].startswith("Freq:")

ts2 = ts.iloc[np.random.randint(0, len(ts) - 1, 400)]
repr(ts2).splitlines()[-1]
