# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
expected = df_ref[["B", "D"]]
expected.index = range(len(expected))

result = pd.read_excel("test1" + read_ext, sheet_name="Sheet1", usecols=usecols)
tm.assert_frame_equal(result, expected, check_names=False)
