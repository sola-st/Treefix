# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH 10390
df = DataFrame(
    date_range("2016-01-01 00:00:00", periods=3, tz="UTC"), columns=["a"]
)
df["b"] = df.a.subtract(Timedelta(seconds=3600))
result = getattr(df, op)(axis=1)
expected = df[expected_col].rename(None)
tm.assert_series_equal(result, expected)
