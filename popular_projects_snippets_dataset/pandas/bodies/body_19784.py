# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
for indexer in self.indexers.values():
    # FIXME: cache results of indexer == -1 checks.
    if (indexer == -1).any():
        exit(True)

exit(False)
