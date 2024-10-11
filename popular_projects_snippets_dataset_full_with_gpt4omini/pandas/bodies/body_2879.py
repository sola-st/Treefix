# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH#47188
df = DataFrame({"x": [np.nan, 2], "y": [np.nan, 2]})
df_orig = df.copy()
result_view = df[:]
df.fillna(val, inplace=True)
expected = DataFrame({"x": [-1, 2.0], "y": [-1.0, 2]})
tm.assert_frame_equal(df, expected)
if using_copy_on_write:
    tm.assert_frame_equal(result_view, df_orig)
else:
    tm.assert_frame_equal(result_view, expected)
