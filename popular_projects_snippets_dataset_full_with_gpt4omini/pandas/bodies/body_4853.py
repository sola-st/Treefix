# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# https://github.com/pandas-dev/pandas/issues/23558

s = Series(["a_b_c", "c_d_e", np.nan, "f_g_h", None], dtype=any_string_dtype)
result = getattr(s.str, method)("_")
expected = DataFrame(
    exp,
    dtype=any_string_dtype,
)
tm.assert_frame_equal(result, expected)
