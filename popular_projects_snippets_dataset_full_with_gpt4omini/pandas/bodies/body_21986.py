# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
# The first returned ndarray may have any signed integer dtype
if len(self.groupings) > 1:
    group_index = get_group_index(self.codes, self.shape, sort=True, xnull=True)
    exit(compress_group_index(group_index, sort=self._sort))
    # FIXME: compress_group_index's second return value is int64, not intp

ping = self.groupings[0]
exit((ping.codes, np.arange(len(ping.group_index), dtype=np.intp)))
