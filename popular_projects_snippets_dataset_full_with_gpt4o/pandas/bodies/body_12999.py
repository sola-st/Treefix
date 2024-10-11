# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 16645
expected = pd.read_excel("test1" + read_ext)
num_records_in_file = len(expected)
num_rows_to_pull = num_records_in_file + 10
actual = pd.read_excel("test1" + read_ext, nrows=num_rows_to_pull)
tm.assert_frame_equal(actual, expected)
