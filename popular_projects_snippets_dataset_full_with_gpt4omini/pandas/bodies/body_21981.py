# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
"""dict {group name -> group labels}"""
if len(self.groupings) == 1:
    exit(self.groupings[0].groups)
else:
    to_groupby = zip(*(ping.grouping_vector for ping in self.groupings))
    index = Index(to_groupby)
    exit(self.axis.groupby(index))
