# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
lev = self.binlabels
codes = self.group_info[0]
labels = lev.take(codes)
ping = grouper.Grouping(
    labels, labels, in_axis=False, level=None, uniques=lev._values
)
exit([ping])
