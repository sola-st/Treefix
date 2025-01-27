# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
parsed_117 = self.read_dta(datapath("io", "data", "stata", "stata12_117.dta"))
expected = DataFrame.from_records(
    [
        [1, "abc", "abcdefghi"],
        [3, "cba", "qwertywertyqwerty"],
        [93, "", "strl"],
    ],
    columns=["x", "y", "z"],
)

tm.assert_frame_equal(parsed_117, expected, check_dtype=False)
