# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
original = DataFrame([datetime(2006, 11, 19, 23, 13, 20)])
original.index.name = "index"
with tm.ensure_clean() as path:
    with tm.assert_produces_warning(InvalidColumnName):
        original.to_stata(path, convert_dates={0: "tc"})

    written_and_read_again = self.read_dta(path)

modified = original.copy()
modified.columns = ["_0"]
modified.index = original.index.astype(np.int32)
tm.assert_frame_equal(written_and_read_again.set_index("index"), modified)
