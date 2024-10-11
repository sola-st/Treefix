# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
s1 = Series(np.arange(4.0), dtype=np.float32)
s2 = Series(np.arange(4.0), dtype=np.float64)
s1[::2] = np.nan
s2[1::2] = np.nan
original = DataFrame({"s1": s1, "s2": s2})
original.index.name = "index"

with tm.ensure_clean() as path:
    original.to_stata(path, version=version)
    written_and_read_again = self.read_dta(path)

written_and_read_again = written_and_read_again.set_index("index")
expected = original.copy()
expected.index = expected.index.astype(np.int32)
tm.assert_frame_equal(written_and_read_again, expected)
