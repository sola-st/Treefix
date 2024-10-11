import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

ss = pd.Series([5, 10, 15], index=pd.MultiIndex.from_tuples([(0, 0), (0, 1), (1, 0)], names=['row', 'column'])) # pragma: no cover
row_levels = ['row'] # pragma: no cover
column_levels = ['column'] # pragma: no cover
def _to_ijv(ss, row_levels, column_levels, sort_labels): # pragma: no cover
    rows = np.array([0, 0, 1])# pragma: no cover
    columns = np.array([0, 1, 0])# pragma: no cover
    v = ss.values# pragma: no cover
    return v, rows, columns, list(set(rows)), list(set(columns)) # pragma: no cover
sort_labels = False # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
from types import SimpleNamespace # pragma: no cover

ss = pd.Series([1, 2, 3], index=pd.MultiIndex.from_tuples([(0, 1), (1, 2), (2, 3)], names=['row', 'col'])) # pragma: no cover
row_levels = ['row'] # pragma: no cover
column_levels = ['col'] # pragma: no cover
sort_labels = True # pragma: no cover
def _to_ijv(ss, row_levels, column_levels, sort_labels):# pragma: no cover
    row_values = ss.index.get_level_values(row_levels[0]).to_numpy()# pragma: no cover
    col_values = ss.index.get_level_values(column_levels[0]).to_numpy()# pragma: no cover
    rows = np.unique(row_values)# pragma: no cover
    cols = np.unique(col_values)# pragma: no cover
    row_map = {val: idx for idx, val in enumerate(rows)}# pragma: no cover
    col_map = {val: idx for idx, val in enumerate(cols)}# pragma: no cover
    i = np.array([row_map[val] for val in row_values])# pragma: no cover
    j = np.array([col_map[val] for val in col_values])# pragma: no cover
    v = ss.values# pragma: no cover
    return v, i, j, rows, cols # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/scipy_sparse.py
from l3.Runtime import _l_
"""
    Convert a sparse Series to a scipy.sparse.coo_matrix using index
    levels row_levels, column_levels as the row and column
    labels respectively. Returns the sparse_matrix, row and column labels.
    """
try:
    import scipy.sparse
    _l_(21816)

except ImportError:
    pass

if ss.index.nlevels < 2:
    _l_(21818)

    raise ValueError("to_coo requires MultiIndex with nlevels >= 2.")
    _l_(21817)
if not ss.index.is_unique:
    _l_(21820)

    raise ValueError(
        "Duplicate index entries are not allowed in to_coo transformation."
    )
    _l_(21819)

# to keep things simple, only rely on integer indexing (not labels)
row_levels = [ss.index._get_level_number(x) for x in row_levels]
_l_(21821)
column_levels = [ss.index._get_level_number(x) for x in column_levels]
_l_(21822)

v, i, j, rows, columns = _to_ijv(
    ss, row_levels=row_levels, column_levels=column_levels, sort_labels=sort_labels
)
_l_(21823)
sparse_matrix = scipy.sparse.coo_matrix(
    (v, (i, j)), shape=(len(rows), len(columns))
)
_l_(21824)
aux = (sparse_matrix, rows, columns)
_l_(21825)
exit(aux)
