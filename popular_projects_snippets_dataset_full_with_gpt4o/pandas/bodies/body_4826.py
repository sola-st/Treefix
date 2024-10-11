# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# expand blank split GH 20067
values = Series([""], name="test", dtype=any_string_dtype)
result = values.str.split(expand=True)
exp = DataFrame([[]], dtype=any_string_dtype)  # NOTE: this is NOT an empty df
tm.assert_frame_equal(result, exp)
