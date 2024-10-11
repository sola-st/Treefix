# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# GH 22676; depr kwarg "pat" in favor of "sep"
s = Series(["a_b_c", "c_d_e", np.nan, "f_g_h"], dtype=any_string_dtype)

expected = getattr(s.str, method)(sep="_")
result = getattr(s.str, method)("_")
tm.assert_frame_equal(result, expected)
