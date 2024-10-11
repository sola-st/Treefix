# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 40442
file_name = "testmultiindex" + read_ext
columns = MultiIndex.from_tuples([("a", "A"), ("b", "B")])
data = [[np.nan, np.nan], [np.nan, np.nan], [1, 3], [2, 4]]
expected = DataFrame(data, columns=columns)
result = pd.read_excel(
    file_name, sheet_name="mi_column_empty_rows", header=[0, 1]
)
tm.assert_frame_equal(result, expected)
