# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
original = DataFrame([["1"], [None]], columns=["foo"])

expected = DataFrame(
    [["1"], [""]],
    index=pd.Index([0, 1], dtype=np.int32, name="index"),
    columns=["foo"],
)

with tm.ensure_clean() as path:
    original.to_stata(path)
    written_and_read_again = self.read_dta(path)

tm.assert_frame_equal(written_and_read_again.set_index("index"), expected)
