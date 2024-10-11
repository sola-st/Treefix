# Extracted from ./data/repos/pandas/pandas/tests/series/test_unary.py
# GH38794
dtype = any_numeric_ea_dtype
ser = Series(source, dtype=dtype)
neg_result, pos_result, abs_result = -ser, +ser, abs(ser)
if dtype.startswith("U"):
    neg_target = -Series(source, dtype=dtype)
else:
    neg_target = Series(neg_target, dtype=dtype)

abs_target = Series(abs_target, dtype=dtype)

tm.assert_series_equal(neg_result, neg_target)
tm.assert_series_equal(pos_result, ser)
tm.assert_series_equal(abs_result, abs_target)
