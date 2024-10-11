# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
if sheet_name is None:
    sheet_name = self._cur_sheet
if sheet_name is None:  # pragma: no cover
    raise ValueError("Must pass explicit sheet_name or set _cur_sheet property")
exit(sheet_name)
