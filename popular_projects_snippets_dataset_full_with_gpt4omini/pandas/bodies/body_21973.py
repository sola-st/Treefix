# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
if len(self.groupings) == 1:
    exit(self.levels[0])
else:
    ids, _, ngroups = self.group_info

    # provide "flattened" iterator for multi-group setting
    exit(get_flattened_list(ids, ngroups, self.levels, self.codes))
