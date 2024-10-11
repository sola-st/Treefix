# Extracted from ./data/repos/pandas/pandas/tests/frame/test_unary.py
# GH#21380
tm.assert_frame_equal(+df, df)
tm.assert_series_equal(+df["a"], df["a"])
