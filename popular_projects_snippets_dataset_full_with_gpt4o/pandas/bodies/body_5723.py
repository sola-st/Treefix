# Extracted from ./data/repos/pandas/pandas/tests/extension/list/array.py
if not isinstance(values, np.ndarray):
    raise TypeError("Need to pass a numpy array as values")
for val in values:
    if not isinstance(val, self.dtype.type) and not pd.isna(val):
        raise TypeError("All values must be of type " + str(self.dtype.type))
self.data = values
