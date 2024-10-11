# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_xlrd.py
# GH 41226
f = io.BytesIO(file_header)
assert inspect_excel_format(f) == "xls"
