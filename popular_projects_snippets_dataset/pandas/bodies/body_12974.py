# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
expected = DataFrame(columns=["col_1", "col_2"])
actual = pd.read_excel("blank_with_header" + read_ext, sheet_name="Sheet1")
tm.assert_frame_equal(actual, expected)
