# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH 27185
df = DataFrame(
    {
        "A": Series([1, 2, NaT], dtype="timedelta64[ns]"),
        "B": Series([1, 2, np.nan], dtype="Int64"),
    }
)
expected = Series({"A": Timedelta(3), "B": 3})
result = df.sum()
tm.assert_series_equal(result, expected)
