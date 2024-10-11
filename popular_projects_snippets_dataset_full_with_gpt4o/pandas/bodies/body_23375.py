# Extracted from ./data/repos/pandas/pandas/core/interchange/column.py
"""
        Note: doesn't deal with extension arrays yet, just assume a regular
        Series/ndarray for now.
        """
if not isinstance(column, pd.Series):
    raise NotImplementedError(f"Columns of type {type(column)} not handled yet")

# Store the column as a private attribute
self._col = column
self._allow_copy = allow_copy
