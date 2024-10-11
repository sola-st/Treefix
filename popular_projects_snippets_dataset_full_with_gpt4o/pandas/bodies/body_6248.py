# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
if box_in_series:
    data = pd.Series(data)
original = data.copy()

data[[0, 1]] = [data[1], data[0]]
assert data[0] == original[1]
assert data[1] == original[0]
