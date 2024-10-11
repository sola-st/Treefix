# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
if box_in_series:
    data = pd.Series(data)
data[[0, 1]] = data[2]
assert data[0] == data[2]
assert data[1] == data[2]
