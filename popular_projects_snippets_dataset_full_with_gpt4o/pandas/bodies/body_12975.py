# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 48706
with pytest.raises(ValueError, match=r" \(sheet: Sheet1\)$"):
    pd.read_excel("blank_with_header" + read_ext, header=[1], sheet_name=None)
with pytest.raises(ZeroDivisionError, match=r" \(sheet: Sheet1\)$"):
    pd.read_excel("test1" + read_ext, usecols=lambda x: 1 / 0, sheet_name=None)
