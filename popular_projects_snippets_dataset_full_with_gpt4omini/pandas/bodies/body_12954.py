# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# see gh-18792
result = pd.read_excel(
    "test1" + read_ext, sheet_name="Sheet4", index_col=index_col
)
expected = DataFrame(
    [["i1", "a", "x"], ["i2", "b", "y"]], columns=["Unnamed: 0", "col1", "col2"]
)
if index_col:
    expected = expected.set_index(expected.columns[index_col])

tm.assert_frame_equal(result, expected)
