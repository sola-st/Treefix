# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
expected_defaults = {
    "xlsx": "openpyxl",
    "xlsm": "openpyxl",
    "xlsb": "pyxlsb",
    "xls": "xlrd",
    "ods": "odf",
}

with pd.ExcelFile("test1" + read_ext) as excel:
    result = excel.engine

if engine is not None:
    expected = engine
else:
    expected = expected_defaults[read_ext[1:]]
assert result == expected
