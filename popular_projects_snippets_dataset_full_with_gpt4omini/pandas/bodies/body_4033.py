# Extracted from ./data/repos/pandas/pandas/tests/frame/test_unary.py
tm.assert_frame_equal(-df, expected)
tm.assert_series_equal(-df["a"], expected["a"])
