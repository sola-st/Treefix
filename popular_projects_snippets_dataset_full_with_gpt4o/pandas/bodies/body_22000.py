# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
ngroups = self.ngroups
obs_group_ids = np.arange(ngroups, dtype=np.intp)
rep = np.diff(np.r_[0, self.bins])

rep = ensure_platform_int(rep)
if ngroups == len(self.bins):
    comp_ids = np.repeat(np.arange(ngroups), rep)
else:
    comp_ids = np.repeat(np.r_[-1, np.arange(ngroups)], rep)

exit((ensure_platform_int(comp_ids),
    obs_group_ids,
    ngroups,))
