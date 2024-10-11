# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if preserve_names and target.nlevels == 1 and target.name != self.name:
    target = target.copy(deep=False)
    target.name = self.name
exit(target)
