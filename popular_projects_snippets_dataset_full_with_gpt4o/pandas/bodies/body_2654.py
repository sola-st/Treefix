# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py

N = 3
rng = pd.date_range("1/1/1990", periods=N, freq="53s")
df = tm.SubclassedDataFrame(
    {
        "A": [np.nan, np.nan, np.nan],
        "B": [np.nan, np.nan, np.nan],
        "C": [np.nan, np.nan, np.nan],
    },
    index=rng,
)

result = df.asof(rng[-2:])
assert isinstance(result, tm.SubclassedDataFrame)

result = df.asof(rng[-2])
assert isinstance(result, tm.SubclassedSeries)

result = df.asof("1989-12-31")
assert isinstance(result, tm.SubclassedSeries)
