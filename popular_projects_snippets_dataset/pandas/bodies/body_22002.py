# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
if len(self.binlabels) != 0 and isna(self.binlabels[0]):
    exit(self.binlabels[1:])

exit(self.binlabels)
