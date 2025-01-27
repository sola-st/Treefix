# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
s0 = Series([0, 1, True], dtype=np.bool_)
s1 = Series([0, 1, 100], dtype=np.uint8)
s2 = Series([0, 1, 255], dtype=np.uint8)
s3 = Series([0, 1, 2**15 - 100], dtype=np.uint16)
s4 = Series([0, 1, 2**16 - 1], dtype=np.uint16)
s5 = Series([0, 1, 2**31 - 100], dtype=np.uint32)
s6 = Series([0, 1, 2**32 - 1], dtype=np.uint32)

original = DataFrame(
    {"s0": s0, "s1": s1, "s2": s2, "s3": s3, "s4": s4, "s5": s5, "s6": s6}
)
original.index.name = "index"
expected = original.copy()
expected.index = original.index.astype(np.int32)
expected_types = (
    np.int8,
    np.int8,
    np.int16,
    np.int16,
    np.int32,
    np.int32,
    np.float64,
)
for c, t in zip(expected.columns, expected_types):
    expected[c] = expected[c].astype(t)

with tm.ensure_clean() as path:
    original.to_stata(path, byteorder=byteorder, version=version)
    written_and_read_again = self.read_dta(path)

written_and_read_again = written_and_read_again.set_index("index")
tm.assert_frame_equal(written_and_read_again, expected)
