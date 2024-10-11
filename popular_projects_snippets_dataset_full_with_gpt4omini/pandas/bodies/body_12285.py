# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
original = self.read_csv(datapath("io", "data", "stata", "stata3.csv"))
original.index.name = "index"
original.index = original.index.astype(np.int32)
original["year"] = original["year"].astype(np.int32)
original["quarter"] = original["quarter"].astype(np.int32)

with tm.ensure_clean() as path:
    original.to_stata(path, convert_dates=None)
    written_and_read_again = self.read_dta(path)
    tm.assert_frame_equal(
        written_and_read_again.set_index("index"),
        original,
        check_index_type=False,
    )
