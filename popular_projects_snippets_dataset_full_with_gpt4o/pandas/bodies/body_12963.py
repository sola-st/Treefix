# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# see gh-20377
basename = "testdtype"

actual = pd.read_excel(basename + read_ext, dtype=dtype)
tm.assert_frame_equal(actual, expected)
