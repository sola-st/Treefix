# Extracted from ./data/repos/pandas/pandas/tests/frame/test_unary.py
# GH#21380
df = pd.DataFrame({"a": df})
expected = pd.DataFrame({"a": expected})
tm.assert_frame_equal(-df, expected)
tm.assert_series_equal(-df["a"], expected["a"])
