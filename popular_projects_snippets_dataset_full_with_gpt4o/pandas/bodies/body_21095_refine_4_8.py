import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

row_levels = [0] # pragma: no cover
column_levels = [1] # pragma: no cover
def _to_ijv(ss, row_levels, column_levels, sort_labels):# pragma: no cover
    v = ss.values# pragma: no cover
    i = ss.index.codes[row_levels[0]]# pragma: no cover
    j = ss.index.codes[column_levels[0]]# pragma: no cover
    rows = list(np.unique(i))# pragma: no cover
    columns = list(np.unique(j))# pragma: no cover
    return v, i, j, rows, columns # pragma: no cover
sort_labels = False # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

ss = pd.Series([1, 2, 3], index=pd.MultiIndex.from_tuples([(0, 0), (1, 1), (2, 2)], names=['row', 'col'])) # pragma: no cover
row_levels = ['row'] # pragma: no cover
column_levels = ['col'] # pragma: no cover
sort_labels = True # pragma: no cover
def _to_ijv(ss, row_levels, column_levels, sort_labels):# pragma: no cover
    rows = ss.index.get_level_values(row_levels[0])# pragma: no cover
    cols = ss.index.get_level_values(column_levels[0])# pragma: no cover
    v = ss.values# pragma: no cover
    row_labels, row_ind = np.unique(rows, return_inverse=True)# pragma: no cover
    col_labels, col_ind = np.unique(cols, return_inverse=True)# pragma: no cover
    return v, row_ind, col_ind, row_labels, col_labels # pragma: no cover
class MockIndex:# pragma: no cover
    def __init__(self, nlevels=2, is_unique=True):# pragma: no cover
        self.nlevels = nlevels# pragma: no cover
        self.is_unique = is_unique# pragma: no cover
    def _get_level_number(self, level):# pragma: no cover
        if level == 'row':# pragma: no cover
            return 0# pragma: no cover
        if level == 'col':# pragma: no cover
            return 1# pragma: no cover
        raise ValueError('Level not found')# pragma: no cover
    def get_level_values(self, level):# pragma: no cover
        if level == 0:# pragma: no cover
            return np.array([0, 1, 2])# pragma: no cover
        if level == 1:# pragma: no cover
            return np.array([0, 1, 2])# pragma: no cover
        raise ValueError('Invalid level') # pragma: no cover

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
