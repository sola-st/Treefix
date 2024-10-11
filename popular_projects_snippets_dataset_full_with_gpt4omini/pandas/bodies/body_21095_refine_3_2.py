import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import scipy.sparse # pragma: no cover

row_levels = ['row'] # pragma: no cover
column_levels = ['column'] # pragma: no cover
_to_ijv = lambda ss, row_levels, column_levels, sort_labels: (ss.values, ss.index.get_level_values(row_levels[0]), ss.index.get_level_values(column_levels[0]), ss.index.levels[0], ss.index.levels[1]) # pragma: no cover
sort_labels = True # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import scipy.sparse # pragma: no cover

row_levels = ['row_index'] # pragma: no cover
column_levels = ['col_index'] # pragma: no cover
_to_ijv = lambda ss, row_levels, column_levels, sort_labels: (ss.values, ss.index.get_level_values(row_levels[0]), ss.index.get_level_values(column_levels[0]), ss.index.levels[0], ss.index.levels[1]) # pragma: no cover
sort_labels = False # pragma: no cover

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
    _l_(10558)

except ImportError:
    pass

if ss.index.nlevels < 2:
    _l_(10560)

    raise ValueError("to_coo requires MultiIndex with nlevels >= 2.")
    _l_(10559)
if not ss.index.is_unique:
    _l_(10562)

    raise ValueError(
        "Duplicate index entries are not allowed in to_coo transformation."
    )
    _l_(10561)

# to keep things simple, only rely on integer indexing (not labels)
row_levels = [ss.index._get_level_number(x) for x in row_levels]
_l_(10563)
column_levels = [ss.index._get_level_number(x) for x in column_levels]
_l_(10564)

v, i, j, rows, columns = _to_ijv(
    ss, row_levels=row_levels, column_levels=column_levels, sort_labels=sort_labels
)
_l_(10565)
sparse_matrix = scipy.sparse.coo_matrix(
    (v, (i, j)), shape=(len(rows), len(columns))
)
_l_(10566)
aux = (sparse_matrix, rows, columns)
_l_(10567)
exit(aux)
