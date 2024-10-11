# Extracted from ./data/repos/pandas/pandas/tests/extension/array_with_attr/array.py
if not isinstance(values, np.ndarray):
    raise TypeError("Need to pass a numpy array of float64 dtype as values")
if not values.dtype == "float64":
    raise TypeError("Need to pass a numpy array of float64 dtype as values")
self.data = values
self.attr = attr
