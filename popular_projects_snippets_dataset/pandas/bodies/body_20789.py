# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
# overridden by RangeIndex

this = self.unique()

indexer = this.get_indexer_for(other)
indexer = indexer.take((indexer != -1).nonzero()[0])

label_diff = np.setdiff1d(np.arange(this.size), indexer, assume_unique=True)

the_diff: MultiIndex | ArrayLike
if isinstance(this, ABCMultiIndex):
    the_diff = this.take(label_diff)
else:
    the_diff = this._values.take(label_diff)
the_diff = _maybe_try_sort(the_diff, sort)

exit(the_diff)
