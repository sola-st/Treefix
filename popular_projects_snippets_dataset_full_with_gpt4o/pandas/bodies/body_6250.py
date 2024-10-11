# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
if box_in_series:
    data = pd.Series(data)
original = data.copy()
data[np.array([], dtype=int)] = []
self.assert_equal(data, original)
