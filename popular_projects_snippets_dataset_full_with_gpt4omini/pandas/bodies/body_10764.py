# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# GH 17382
df = DataFrame({"time": pd.to_timedelta(range(10)), "cat": ["A", "B"] * 5})
result = df.groupby("cat")["time"].mean()
expected = Series(
    pd.to_timedelta([4, 5]), name="time", index=Index(["A", "B"], name="cat")
)
tm.assert_series_equal(result, expected)
