# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# GH 8473
dates = date_range("1/1/2000", periods=8)
df_orig = DataFrame(
    np.random.randn(8, 4), index=dates, columns=["A", "B", "C", "D"]
)

expected = pd.concat(
    [df_orig, DataFrame({"A": 7}, index=dates[-1:] + dates.freq)], sort=True
)
df = df_orig.copy()
df.loc[dates[-1] + dates.freq, "A"] = 7
tm.assert_frame_equal(df, expected)
df = df_orig.copy()
df.at[dates[-1] + dates.freq, "A"] = 7
tm.assert_frame_equal(df, expected)

exp_other = DataFrame({0: 7}, index=dates[-1:] + dates.freq)
expected = pd.concat([df_orig, exp_other], axis=1)

df = df_orig.copy()
df.loc[dates[-1] + dates.freq, 0] = 7
tm.assert_frame_equal(df, expected)
df = df_orig.copy()
df.at[dates[-1] + dates.freq, 0] = 7
tm.assert_frame_equal(df, expected)
