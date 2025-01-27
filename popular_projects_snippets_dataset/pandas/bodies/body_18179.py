# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#8932, GH#22163
ts = fixed_now_ts
obj = np.array(range(5))
obj = tm.box_expected(obj, box_with_array)

assert_invalid_comparison(obj, ts, box_with_array)
