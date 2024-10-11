# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
values = Series(["a b c", "a b", "", " "], name="test", dtype=any_string_dtype)
result = values.str.split(expand=True)
exp = DataFrame(
    [
        ["a", "b", "c"],
        ["a", "b", np.nan],
        [np.nan, np.nan, np.nan],
        [np.nan, np.nan, np.nan],
    ],
    dtype=any_string_dtype,
)
tm.assert_frame_equal(result, exp)
