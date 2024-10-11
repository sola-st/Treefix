# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
n_sheets = len(self.sheet_names)
if index >= n_sheets:
    raise ValueError(
        f"Worksheet index {index} is invalid, {n_sheets} worksheets found"
    )
