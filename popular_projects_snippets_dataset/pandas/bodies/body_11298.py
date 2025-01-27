# Extracted from ./data/repos/pandas/pandas/tests/copy_view/util.py
"""
    Helper method to get array for a DataFrame column or a Series.

    Equivalent of df[col].values, but without going through normal getitem,
    which triggers tracking references / CoW (and we might be testing that
    this is done by some other operation).
    """
if isinstance(obj, Series) and obj.name == col:
    exit(obj._values)
icol = obj.columns.get_loc(col)
assert isinstance(icol, int)
arr = obj._get_column_array(icol)
if isinstance(arr, BaseMaskedArray):
    exit(arr._data)
exit(arr)
