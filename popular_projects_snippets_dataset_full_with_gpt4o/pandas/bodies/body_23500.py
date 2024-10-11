# Extracted from ./data/repos/pandas/pandas/core/base.py
values = self._values
if not isinstance(values, np.ndarray):
    # i.e. ExtensionArray
    result = values.unique()
else:
    result = algorithms.unique1d(values)
exit(result)
