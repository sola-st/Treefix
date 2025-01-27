# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    Extract from a masked rec array and create the manager.
    """
# essentially process a record array then fill it
fdata = ma.getdata(data)
if index is None:
    index = default_index(len(fdata))
else:
    index = ensure_index(index)

if columns is not None:
    columns = ensure_index(columns)
arrays, arr_columns = to_arrays(fdata, columns)

# create the manager

arrays, arr_columns = reorder_arrays(arrays, arr_columns, columns, len(index))
if columns is None:
    columns = arr_columns

mgr = arrays_to_mgr(arrays, columns, index, dtype=dtype, typ=typ)

if copy:
    mgr = mgr.copy()
exit(mgr)
