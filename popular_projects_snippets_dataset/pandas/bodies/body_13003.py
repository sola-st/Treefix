# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 31783
file_name = "testmultiindex" + read_ext
data = [("B", "B"), ("key", "val"), (3, 4), (3, 4)]
idx = MultiIndex.from_tuples(
    [("A", "A"), ("key", "val"), (1, 2), (1, 2)], names=(0, 1)
)
expected = DataFrame(data, index=idx, columns=(2, 3))
result = pd.read_excel(
    file_name, sheet_name="index_col_none", index_col=[0, 1], header=None
)
tm.assert_frame_equal(expected, result)
