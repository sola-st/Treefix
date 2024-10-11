# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
indexer = np.delete(np.arange(len(self)), loc)
exit(self.take(indexer))
