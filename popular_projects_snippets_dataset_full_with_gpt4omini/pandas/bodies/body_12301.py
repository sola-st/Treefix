# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
s0 = Series([1, 99], dtype=np.int8)
s1 = Series([1, 127], dtype=np.int8)
s2 = Series([1, 2**15 - 1], dtype=np.int16)
s3 = Series([1, 2**63 - 1], dtype=np.int64)
original = DataFrame({"s0": s0, "s1": s1, "s2": s2, "s3": s3})
original.index.name = "index"
with tm.ensure_clean() as path:
    with tm.assert_produces_warning(PossiblePrecisionLoss):
        original.to_stata(path)

    written_and_read_again = self.read_dta(path)

modified = original.copy()
modified["s1"] = Series(modified["s1"], dtype=np.int16)
modified["s2"] = Series(modified["s2"], dtype=np.int32)
modified["s3"] = Series(modified["s3"], dtype=np.float64)
modified.index = original.index.astype(np.int32)
tm.assert_frame_equal(written_and_read_again.set_index("index"), modified)
