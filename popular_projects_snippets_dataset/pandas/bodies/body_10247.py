# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH 11616
# Test that column selection returns output in correct timezone.
np.random.seed(42)
df = DataFrame(
    {
        "factor": np.random.randint(0, 3, size=60),
        "time": date_range("01/01/2000 00:00", periods=60, freq="s", tz="UTC"),
    }
)
df1 = df.groupby("factor").max()["time"]
df2 = df.groupby("factor")["time"].max()
tm.assert_series_equal(df1, df2)
