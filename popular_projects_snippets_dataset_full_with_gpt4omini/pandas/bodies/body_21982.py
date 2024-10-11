# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
# return if my group orderings are monotonic
exit(Index(self.group_info[0]).is_monotonic_increasing)
