# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
s1 = Series(2**9, dtype=np.int16)
s2 = Series(2**17, dtype=np.int32)
s3 = Series(2**33, dtype=np.int64)
original = DataFrame({"int16": s1, "int32": s2, "int64": s3})
original.index.name = "index"

formatted = original
formatted["int64"] = formatted["int64"].astype(np.float64)

with tm.ensure_clean() as path:
    original.to_stata(path)
    written_and_read_again = self.read_dta(path)

expected = formatted.copy()
expected.index = expected.index.astype(np.int32)
tm.assert_frame_equal(written_and_read_again.set_index("index"), expected)
