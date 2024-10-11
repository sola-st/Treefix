# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
indexer, to_sort = self._indexer_and_to_sort
exit([line.take(indexer) for line in to_sort])
