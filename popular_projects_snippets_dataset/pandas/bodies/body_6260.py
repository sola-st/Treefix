# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
# wrong length
mask = np.array([True, False])

if box_in_series:
    data = pd.Series(data)

with pytest.raises(IndexError, match="wrong length"):
    data[mask] = data[0]

mask = pd.array(mask, dtype="boolean")
with pytest.raises(IndexError, match="wrong length"):
    data[mask] = data[0]
