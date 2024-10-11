# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
indexer, _ = self._indexer_and_to_sort

sorted_values = algos.take_nd(values, indexer, axis=0)
exit(sorted_values)
