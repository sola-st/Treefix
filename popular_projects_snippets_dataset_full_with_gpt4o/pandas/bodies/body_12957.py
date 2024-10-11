# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py

parsed = pd.read_excel("test2" + read_ext, sheet_name="Sheet1")
expected = DataFrame([["aaaa", "bbbbb"]], columns=["Test", "Test1"])
tm.assert_frame_equal(parsed, expected)
