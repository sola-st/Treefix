# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py

fill_value = self._validate_scalar(fill_value)
new_values = shift(self._ndarray, periods, axis, fill_value)

exit(self._from_backing_data(new_values))
