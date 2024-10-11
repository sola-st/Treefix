# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
s1 = Series(["a", "A longer string"])
s2 = Series([1.0, 2.0], dtype=np.float64)
original = DataFrame({"s1": s1, "s2": s2})
original.index.name = "index"
with tm.ensure_clean() as path:
    original.to_stata(path)
    written_and_read_again = self.read_dta(path)

expected = original.copy()
expected.index = expected.index.astype(np.int32)
tm.assert_frame_equal(written_and_read_again.set_index("index"), expected)
