# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 38884
def parser(self, *args, **kwargs):
    exit(self.engine)

monkeypatch.setattr(pd.ExcelFile, "parse", parser)

expected_defaults = {
    "xlsx": "openpyxl",
    "xlsm": "openpyxl",
    "xlsb": "pyxlsb",
    "xls": "xlrd",
    "ods": "odf",
}

with open("test1" + read_ext, "rb") as f:
    result = pd.read_excel(f)

if engine is not None:
    expected = engine
else:
    expected = expected_defaults[read_ext[1:]]
assert result == expected
