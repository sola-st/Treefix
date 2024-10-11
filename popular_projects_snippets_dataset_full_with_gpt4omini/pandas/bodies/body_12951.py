# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
msg = "Invalid column name: E1"

with pytest.raises(ValueError, match=msg):
    pd.read_excel("test1" + read_ext, sheet_name="Sheet1", usecols="D:E1")
