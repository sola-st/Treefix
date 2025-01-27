# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
if name not in self.sheet_names:
    raise ValueError(f"Worksheet named '{name}' not found")
