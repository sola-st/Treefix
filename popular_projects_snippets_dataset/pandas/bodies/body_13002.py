# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
with pytest.raises(TypeError, match="but 3 positional arguments"):
    pd.read_excel("test1" + read_ext, "Sheet1", 0)
