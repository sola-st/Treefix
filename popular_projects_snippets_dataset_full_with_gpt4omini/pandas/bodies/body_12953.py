# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# see gh-9208
result = pd.read_excel(
    "test1" + read_ext, sheet_name="Sheet3", index_col=["A", "B", "C"]
)
expected = DataFrame(
    columns=["D", "E", "F"],
    index=MultiIndex(levels=[[]] * 3, codes=[[]] * 3, names=["A", "B", "C"]),
)
tm.assert_frame_equal(result, expected)
