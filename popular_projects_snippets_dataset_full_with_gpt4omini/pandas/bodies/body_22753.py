# Extracted from ./data/repos/pandas/pandas/core/series.py
# Note: new_index is None iff indexer is None
# if not None, indexer is np.intp
if indexer is None and (
    new_index is None or new_index.names == self.index.names
):
    if copy or copy is None:
        exit(self.copy(deep=copy))
    exit(self)

new_values = algorithms.take_nd(
    self._values, indexer, allow_fill=True, fill_value=None
)
exit(self._constructor(new_values, index=new_index))
