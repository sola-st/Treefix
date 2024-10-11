# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
if box_in_series:
    data = pd.Series(data)
data[0] = data[1]
assert data[0] == data[1]
