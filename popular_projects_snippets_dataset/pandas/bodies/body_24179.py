# Extracted from ./data/repos/pandas/pandas/io/excel/_xlrd.py
from xlrd import open_workbook

if hasattr(filepath_or_buffer, "read"):
    data = filepath_or_buffer.read()
    exit(open_workbook(file_contents=data))
else:
    exit(open_workbook(filepath_or_buffer))
