# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 33476
idx = Index(["Z"], name="I2")
cols = MultiIndex.from_tuples([("A", "B"), ("A", "B.1")], names=["I11", "I12"])
expected = DataFrame([[1, 3]], index=idx, columns=cols, dtype="int64")
result = pd.read_excel(
    filename, sheet_name="Sheet1", index_col=0, header=[0, 1]
)
tm.assert_frame_equal(expected, result)
