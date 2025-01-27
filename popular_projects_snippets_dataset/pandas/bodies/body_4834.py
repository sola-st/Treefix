# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
s = Series(
    ["some_splits", "with_index"], index=["preserve", "me"], dtype=any_string_dtype
)
result = s.str.split("_", expand=True)
exp = DataFrame(
    {0: ["some", "with"], 1: ["splits", "index"]},
    index=["preserve", "me"],
    dtype=any_string_dtype,
)
tm.assert_frame_equal(result, exp)

with pytest.raises(ValueError, match="expand must be"):
    s.str.split("_", expand="not_a_boolean")
