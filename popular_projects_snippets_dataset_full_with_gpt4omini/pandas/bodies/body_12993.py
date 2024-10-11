# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# see gh-11733.
#
# Don't try to parse a header name if there isn't one.
mi_file = "testmultiindex" + read_ext
result = pd.read_excel(mi_file, sheet_name="index_col_none", header=[0, 1])

exp_columns = MultiIndex.from_product([("A", "B"), ("key", "val")])
expected = DataFrame([[1, 2, 3, 4]] * 2, columns=exp_columns)
tm.assert_frame_equal(result, expected)
