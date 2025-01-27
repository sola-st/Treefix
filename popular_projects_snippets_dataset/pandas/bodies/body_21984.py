# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
comp_ids, obs_group_ids = self._get_compressed_codes()

ngroups = len(obs_group_ids)
comp_ids = ensure_platform_int(comp_ids)

exit((comp_ids, obs_group_ids, ngroups))
