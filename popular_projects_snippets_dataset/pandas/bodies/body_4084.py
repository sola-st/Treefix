# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
df = DataFrame(
    {
        "A": np.arange(3),
        "B": date_range("2016-01-01", periods=3),
        "C": pd.timedelta_range("1D", periods=3),
    }
)

# datetime(tz) and timedelta work
result = df.mean(numeric_only=False)
expected = Series({"A": 1, "B": df.loc[1, "B"], "C": df.loc[1, "C"]})
tm.assert_series_equal(result, expected)

# mean of period is not allowed
df["D"] = pd.period_range("2016", periods=3, freq="A")

with pytest.raises(TypeError, match="mean is not implemented for Period"):
    df.mean(numeric_only=False)
