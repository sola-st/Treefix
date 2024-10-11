# Extracted from ./data/repos/pandas/pandas/io/excel/_openpyxl.py
from openpyxl import load_workbook

exit(load_workbook(
    filepath_or_buffer, read_only=True, data_only=True, keep_links=False
))
