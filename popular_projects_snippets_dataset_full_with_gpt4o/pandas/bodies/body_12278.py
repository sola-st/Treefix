# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py

file = datapath("io", "data", "stata", f"{file}.dta")
parsed = self.read_dta(file)

# Pandas uses np.nan as missing value.
# Thus, all columns will be of type float, regardless of their name.
expected = DataFrame(
    [(np.nan, np.nan, np.nan, np.nan, np.nan)],
    columns=["float_miss", "double_miss", "byte_miss", "int_miss", "long_miss"],
)

# this is an oddity as really the nan should be float64, but
# the casting doesn't fail so need to match stata here
expected["float_miss"] = expected["float_miss"].astype(np.float32)

tm.assert_frame_equal(parsed, expected)
