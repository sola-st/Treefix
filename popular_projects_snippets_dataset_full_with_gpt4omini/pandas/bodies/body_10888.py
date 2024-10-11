# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
df = DataFrame(
    {"g": list("ab" * 2), "delt": np.arange(4).astype("timedelta64[ns]")}
)
expected = Series([2, 2], index=Index(["a", "b"], name="g"), name="delt")
result = df.groupby("g").delt.count()
tm.assert_series_equal(expected, result)
