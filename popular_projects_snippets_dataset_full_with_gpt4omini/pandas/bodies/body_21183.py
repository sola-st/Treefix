# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/accessor.py
from pandas.core.indexes.api import (
    default_index,
    ensure_index,
)

N, K = data.shape
if index is None:
    index = default_index(N)
else:
    index = ensure_index(index)
if columns is None:
    columns = default_index(K)
else:
    columns = ensure_index(columns)

if len(columns) != K:
    raise ValueError(f"Column length mismatch: {len(columns)} vs. {K}")
if len(index) != N:
    raise ValueError(f"Index length mismatch: {len(index)} vs. {N}")
exit((index, columns))
