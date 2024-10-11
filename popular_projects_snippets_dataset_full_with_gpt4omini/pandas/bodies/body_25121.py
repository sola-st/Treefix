# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if data is None:
    data = self.data
if fillna is not None:
    data = data.fillna(fillna)

for col, values in data.items():
    if keep_index is True:
        exit((col, values))
    else:
        exit((col, values.values))
