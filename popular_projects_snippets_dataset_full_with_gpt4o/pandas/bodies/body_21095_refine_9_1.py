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
import sys # pragma: no cover

class FakeScipySparse:# pragma: no cover
    class coo_matrix:# pragma: no cover
        def __init__(self, data, shape):# pragma: no cover
            self.data = data# pragma: no cover
            self.shape = shape# pragma: no cover
            self.row = data[1][0]# pragma: no cover
            self.col = data[1][1]# pragma: no cover
            self.data_value = data[0]# pragma: no cover
# pragma: no cover
        def toarray(self):# pragma: no cover
            dense = np.zeros(self.shape)# pragma: no cover
            for r, c, v in zip(self.row, self.col, self.data_value):# pragma: no cover
                dense[r, c] = v# pragma: no cover
            return dense# pragma: no cover
# pragma: no cover
sys.modules['scipy'] = type('Mock', (object,), {'sparse': FakeScipySparse}) # pragma: no cover
ss = pd.Series([1, 2, 3], index=pd.MultiIndex.from_tuples([(0, 0), (1, 1), (2, 0)], names=['row', 'column'])) # pragma: no cover
row_levels = ['row'] # pragma: no cover
column_levels = ['column'] # pragma: no cover
def _to_ijv(ss, row_levels, column_levels, sort_labels):# pragma: no cover
    rows = np.array([0, 1, 2])# pragma: no cover
    columns = np.array([0, 1, 0])# pragma: no cover
    v = ss.values# pragma: no cover
    return v, rows, columns, list(set(rows)), list(set(columns)) # pragma: no cover
sort_labels = True # pragma: no cover

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
