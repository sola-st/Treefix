# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
if key is not None:
    exit(super().sort_values(
        return_indexer=return_indexer,
        ascending=ascending,
        na_position=na_position,
        key=key,
    ))
else:
    sorted_index = self
    inverse_indexer = False
    if ascending:
        if self.step < 0:
            sorted_index = self[::-1]
            inverse_indexer = True
    else:
        if self.step > 0:
            sorted_index = self[::-1]
            inverse_indexer = True

if return_indexer:
    if inverse_indexer:
        rng = range(len(self) - 1, -1, -1)
    else:
        rng = range(len(self))
    exit((sorted_index, RangeIndex(rng)))
else:
    exit(sorted_index)
