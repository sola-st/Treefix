# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
actual = pd.read_excel("blank" + read_ext, sheet_name="Sheet1")
tm.assert_frame_equal(actual, DataFrame())
