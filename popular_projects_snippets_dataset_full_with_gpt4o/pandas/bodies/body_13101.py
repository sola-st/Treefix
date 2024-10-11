# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-15160
expected = DataFrame([[1, 2], [3, 4]], columns=["col1", "col2"])
expected.to_excel(path, "Sheet1", freeze_panes=(1, 1))

result = pd.read_excel(path, index_col=0)
tm.assert_frame_equal(result, expected)
