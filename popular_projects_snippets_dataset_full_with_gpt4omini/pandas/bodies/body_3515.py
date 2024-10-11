# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_update.py
# GH#47188
df = DataFrame({"A": ["1", np.nan], "B": ["100", np.nan]})
df2 = DataFrame({"A": ["a", "x"], "B": ["100", "200"]})
df2_orig = df2.copy()
result_view = df2[:]
df2.update(df)
expected = DataFrame({"A": ["1", "x"], "B": ["100", "200"]})
tm.assert_frame_equal(df2, expected)
if using_copy_on_write:
    tm.assert_frame_equal(result_view, df2_orig)
else:
    tm.assert_frame_equal(result_view, expected)
