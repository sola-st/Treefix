# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#37392
tdi = pd.timedelta_range("1 Day", periods=10)
df = DataFrame({"A": tdi, "B": tdi}, copy=True)
df.iloc[-2, -1] = pd.NaT

result = df.std(skipna=False)
expected = Series(
    [df["A"].std(), pd.NaT], index=["A", "B"], dtype="timedelta64[ns]"
)
tm.assert_series_equal(result, expected)

result = df.std(axis=1, skipna=False)
expected = Series([pd.Timedelta(0)] * 8 + [pd.NaT, pd.Timedelta(0)])
tm.assert_series_equal(result, expected)
