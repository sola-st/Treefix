# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
mask = pd.array(np.zeros(data.shape, dtype="bool"), dtype="boolean")
mask[:3] = True
mask[3:5] = pd.NA

if box_in_series:
    data = pd.Series(data)

data[mask] = data[0]

assert (data[:3] == data[0]).all()
