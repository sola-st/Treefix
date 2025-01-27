# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
codes = self.codes
ids, obs_ids, _ = self.group_info
exit(decons_obs_group_ids(ids, obs_ids, self.shape, codes, xnull=True))
