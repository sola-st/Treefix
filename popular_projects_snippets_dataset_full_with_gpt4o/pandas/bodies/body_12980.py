# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 39250
msg = "Worksheet index 3 is invalid|Worksheet named 'Sheet4' not found"
with pytest.raises(ValueError, match=msg):
    pd.read_excel("blank" + read_ext, sheet_name=sheet_name)
