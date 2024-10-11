# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# GH#1134
s1 = Series([True, False, True], index=list("ABC"), name="x")
s2 = Series([True, True, False], index=list("ABD"), name="x")

exp = Series([True, False, False, False], index=list("ABCD"), name="x")
tm.assert_series_equal(s1 & s2, exp)
tm.assert_series_equal(s2 & s1, exp)

# True | np.nan => True
exp_or1 = Series([True, True, True, False], index=list("ABCD"), name="x")
tm.assert_series_equal(s1 | s2, exp_or1)
# np.nan | True => np.nan, filled with False
exp_or = Series([True, True, False, False], index=list("ABCD"), name="x")
tm.assert_series_equal(s2 | s1, exp_or)

# DataFrame doesn't fill nan with False
tm.assert_frame_equal(s1.to_frame() & s2.to_frame(), exp.to_frame())
tm.assert_frame_equal(s2.to_frame() & s1.to_frame(), exp.to_frame())

exp = DataFrame({"x": [True, True, np.nan, np.nan]}, index=list("ABCD"))
tm.assert_frame_equal(s1.to_frame() | s2.to_frame(), exp_or1.to_frame())
tm.assert_frame_equal(s2.to_frame() | s1.to_frame(), exp_or.to_frame())

# different length
s3 = Series([True, False, True], index=list("ABC"), name="x")
s4 = Series([True, True, True, True], index=list("ABCD"), name="x")

exp = Series([True, False, True, False], index=list("ABCD"), name="x")
tm.assert_series_equal(s3 & s4, exp)
tm.assert_series_equal(s4 & s3, exp)

# np.nan | True => np.nan, filled with False
exp_or1 = Series([True, True, True, False], index=list("ABCD"), name="x")
tm.assert_series_equal(s3 | s4, exp_or1)
# True | np.nan => True
exp_or = Series([True, True, True, True], index=list("ABCD"), name="x")
tm.assert_series_equal(s4 | s3, exp_or)

tm.assert_frame_equal(s3.to_frame() & s4.to_frame(), exp.to_frame())
tm.assert_frame_equal(s4.to_frame() & s3.to_frame(), exp.to_frame())

tm.assert_frame_equal(s3.to_frame() | s4.to_frame(), exp_or1.to_frame())
tm.assert_frame_equal(s4.to_frame() | s3.to_frame(), exp_or.to_frame())
