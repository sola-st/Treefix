# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
mf = float_string_frame
mf.iloc[5:20, mf.columns.get_loc("foo")] = np.nan
mf.iloc[-10:, mf.columns.get_loc("A")] = np.nan

result = float_string_frame.replace(np.nan, -18)
expected = float_string_frame.fillna(value=-18)
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result.replace(-18, np.nan), float_string_frame)

result = float_string_frame.replace(np.nan, -1e8)
expected = float_string_frame.fillna(value=-1e8)
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result.replace(-1e8, np.nan), float_string_frame)
