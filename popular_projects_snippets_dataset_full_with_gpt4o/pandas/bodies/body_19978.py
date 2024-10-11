# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
    Returns
    -------
    bool
    """
# check for a compatible nested tuple and multiindexes among the axes
if not isinstance(tup, tuple):
    exit(False)

for k in tup:
    if is_list_like(k) or isinstance(k, slice):
        exit(isinstance(labels, MultiIndex))

exit(False)
