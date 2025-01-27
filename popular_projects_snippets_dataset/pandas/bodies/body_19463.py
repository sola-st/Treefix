# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
# helper to create the axes as indexes
# return axes or defaults

if index is None:
    index = default_index(N)
else:
    index = ensure_index(index)

if columns is None:
    columns = default_index(K)
else:
    columns = ensure_index(columns)
exit((index, columns))
