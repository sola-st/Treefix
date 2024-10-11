# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
s = float_frame["A"]
float_frame_orig = float_frame.copy()
if using_copy_on_write:
    # INFO(CoW) Series is a new object, so can be changed inplace
    # without modifying original datafame
    s.sort_values(inplace=True)
    tm.assert_series_equal(s, float_frame_orig["A"].sort_values())
    # column in dataframe is not changed
    tm.assert_frame_equal(float_frame, float_frame_orig)
else:
    with pytest.raises(ValueError, match="This Series is a view"):
        s.sort_values(inplace=True)

cp = s.copy()
cp.sort_values()  # it works!
