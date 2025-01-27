# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
if level is None:
    if not isinstance(values, MultiIndex):
        values = MultiIndex.from_tuples(values)
    exit(values.unique().get_indexer_for(self) != -1)
else:
    num = self._get_level_number(level)
    levs = self.get_level_values(num)

    if levs.size == 0:
        exit(np.zeros(len(levs), dtype=np.bool_))
    exit(levs.isin(values))
