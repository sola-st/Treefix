# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
# GH 7764
s = Series(range(4))
s_expected = Series(np.nan, index=s.index)
df = DataFrame([[1, 5], [3, 2], [3, 9], [-1, 0]], columns=["A", "B"])
df_expected = DataFrame(np.nan, index=df.index, columns=df.columns)

s_result = f(s)
tm.assert_series_equal(s_result, s_expected)

df_result = f(df)
tm.assert_frame_equal(df_result, df_expected)
