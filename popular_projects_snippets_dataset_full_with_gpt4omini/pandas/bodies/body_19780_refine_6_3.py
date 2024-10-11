import numpy as np # pragma: no cover

axes = [np.array([])] # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

mgrs_indexers = [(pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['A', 'B']), {0: np.array([1, 0]), 1: np.array([1, 0])})] # pragma: no cover
axes = [np.array(['A', 'B']), np.array(['A', 'B'])] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
from l3.Runtime import _l_
"""
    Reindex along columns so that all of the BlockManagers being concatenated
    have matching columns.

    Columns added in this reindexing have dtype=np.void, indicating they
    should be ignored when choosing a column's final dtype.
    """
new_mgrs_indexers: list[tuple[BlockManager, dict[int, np.ndarray]]] = []
_l_(10837)

for mgr, indexers in mgrs_indexers:
    _l_(10841)

    # For axis=0 (i.e. columns) we use_na_proxy and only_slice, so this
    #  is a cheap reindexing.
    for i, indexer in indexers.items():
        _l_(10839)

        mgr = mgr.reindex_indexer(
            axes[i],
            indexers[i],
            axis=i,
            copy=False,
            only_slice=True,  # only relevant for i==0
            allow_dups=True,
            use_na_proxy=True,  # only relevant for i==0
        )
        _l_(10838)
    new_mgrs_indexers.append((mgr, {}))
    _l_(10840)
aux = new_mgrs_indexers
_l_(10842)
exit(aux)
