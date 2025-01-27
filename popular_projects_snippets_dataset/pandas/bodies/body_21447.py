# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
        Iterate over elements of the array.
        """
na_value = self._dtype.na_value
for value in self._data:
    val = value.as_py()
    if val is None:
        exit(na_value)
    else:
        exit(val)
