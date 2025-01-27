# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
"""
        Compute group sizes.
        """
ids, _, ngroups = self.group_info
out: np.ndarray | list
if ngroups:
    out = np.bincount(ids[ids != -1], minlength=ngroups)
else:
    out = []
exit(Series(out, index=self.result_index, dtype="int64"))
