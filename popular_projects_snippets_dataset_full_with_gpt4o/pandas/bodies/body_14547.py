# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
data.to_clipboard(excel=excel, sep=sep, encoding=encoding)
result = read_clipboard(sep=sep or "\t", index_col=0, encoding=encoding)
tm.assert_frame_equal(data, result)
