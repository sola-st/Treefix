# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
for i, val in enumerate(values):
    if is_float(val):
        if np.isnan(val):
            values[i] = DecimalDtype.na_value
        else:
            values[i] = DecimalDtype.type(val)
    elif not isinstance(val, decimal.Decimal):
        raise TypeError("All values must be of type " + str(decimal.Decimal))
values = np.asarray(values, dtype=object)

self._data = values
# Some aliases for common attribute names to ensure pandas supports
# these
self._items = self.data = self._data
# those aliases are currently not working due to assumptions
# in internal code (GH-20735)
# self._values = self.values = self.data
self._dtype = DecimalDtype(context)
