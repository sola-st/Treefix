# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
s = Series(["some_equal_splits", "with_no_nans"], dtype=any_string_dtype)
result = s.str.rsplit("_", expand=True)
exp = DataFrame(
    {0: ["some", "with"], 1: ["equal", "no"], 2: ["splits", "nans"]},
    dtype=any_string_dtype,
)
tm.assert_frame_equal(result, exp)

result = s.str.rsplit("_", expand=True, n=2)
exp = DataFrame(
    {0: ["some", "with"], 1: ["equal", "no"], 2: ["splits", "nans"]},
    dtype=any_string_dtype,
)
tm.assert_frame_equal(result, exp)

result = s.str.rsplit("_", expand=True, n=1)
exp = DataFrame(
    {0: ["some_equal", "with_no"], 1: ["splits", "nans"]}, dtype=any_string_dtype
)
tm.assert_frame_equal(result, exp)
