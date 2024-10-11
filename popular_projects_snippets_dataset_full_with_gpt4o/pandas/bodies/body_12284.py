# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
original = DataFrame(
    [(np.nan, np.nan, np.nan, np.nan, np.nan)],
    columns=["float_miss", "double_miss", "byte_miss", "int_miss", "long_miss"],
)
original.index.name = "index"

with tm.ensure_clean() as path:
    original.to_stata(path, convert_dates=None)
    written_and_read_again = self.read_dta(path)

expected = original.copy()
expected.index = expected.index.astype(np.int32)
tm.assert_frame_equal(written_and_read_again.set_index("index"), expected)
