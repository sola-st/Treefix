# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
s = Series(
    ["some_unequal_splits", "one_of_these_things_is_not"], dtype=any_string_dtype
)
result = s.str.split("_", expand=True)
exp = DataFrame(
    {
        0: ["some", "one"],
        1: ["unequal", "of"],
        2: ["splits", "these"],
        3: [np.nan, "things"],
        4: [np.nan, "is"],
        5: [np.nan, "not"],
    },
    dtype=any_string_dtype,
)
tm.assert_frame_equal(result, exp)
