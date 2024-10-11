import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import MultiIndex # pragma: no cover

ss = pd.Series([1, 2, 3], index=MultiIndex.from_tuples([(0, 1), (1, 2), (2, 3)])) # pragma: no cover
row_levels = [0] # pragma: no cover
column_levels = [1] # pragma: no cover
def _to_ijv(series, row_levels, column_levels, sort_labels):# pragma: no cover
    values = np.array(series)# pragma: no cover
    rows = range(len(values))# pragma: no cover
    cols = range(len(values))# pragma: no cover
    rows_labels = list(set(series.index.get_level_values(row_levels[0])))# pragma: no cover
    cols_labels = list(set(series.index.get_level_values(column_levels[0])))# pragma: no cover
    return values, rows, cols, rows_labels, cols_labels # pragma: no cover
sort_labels = False # pragma: no cover
ss.index = MultiIndex.from_tuples([(0, 'a'), (1, 'b'), (2, 'c')]) # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

ss = pd.Series([1, 2, 3], index=pd.MultiIndex.from_tuples([(0, 1), (1, 2), (2, 3)])) # pragma: no cover
row_levels = [0] # pragma: no cover
column_levels = [1] # pragma: no cover
def _to_ijv(series, row_levels, column_levels, sort_labels):# pragma: no cover
    values = np.array(series)# pragma: no cover
    if sort_labels:# pragma: no cover
        row_unique = np.unique(series.index.get_level_values(row_levels[0]))# pragma: no cover
        col_unique = np.unique(series.index.get_level_values(column_levels[0]))# pragma: no cover
    else:# pragma: no cover
        row_unique = series.index.get_level_values(row_levels[0])# pragma: no cover
        col_unique = series.index.get_level_values(column_levels[0])# pragma: no cover
    row_mapping = {val: i for i, val in enumerate(row_unique)}# pragma: no cover
    col_mapping = {val: i for i, val in enumerate(col_unique)}# pragma: no cover
    rows = np.array([row_mapping[val] for val in series.index.get_level_values(row_levels[0])])# pragma: no cover
    cols = np.array([col_mapping[val] for val in series.index.get_level_values(column_levels[0])])# pragma: no cover
    return values, rows, cols, row_unique, col_unique # pragma: no cover
sort_labels = True # pragma: no cover
ss.index = pd.MultiIndex.from_tuples([(0, 'a'), (1, 'b'), (2, 'c')]) # pragma: no cover
class scipy:# pragma: no cover
    class sparse:# pragma: no cover
        @staticmethod# pragma: no cover
        def coo_matrix(*args, **kwargs):# pragma: no cover
            return type('Mock', (object,), {})() # pragma: no cover

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
