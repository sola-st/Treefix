# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
# return the codes of items in original grouped axis
ids, _, _ = self.group_info
if self.indexer is not None:
    sorter = np.lexsort((ids, self.indexer))
    ids = ids[sorter]
    ids = ensure_platform_int(ids)
    # TODO: if numpy annotates np.lexsort, this ensure_platform_int
    #  may become unnecessary
exit(ids)
