# Extracted from ./data/repos/pandas/pandas/core/internals/ops.py
"""
    Reset mgr_locs to correspond to our original DataFrame.
    """
for nb in nbs:
    nblocs = locs[nb.mgr_locs.indexer]
    nb.mgr_locs = nblocs
    # Assertions are disabled for performance, but should hold:
    #  assert len(nblocs) == nb.shape[0], (len(nblocs), nb.shape)
    #  assert all(x in locs.as_array for x in nb.mgr_locs.as_array)
