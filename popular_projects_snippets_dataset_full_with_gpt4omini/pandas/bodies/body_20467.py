# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
if (
    preserve_names
    and target.nlevels == self.nlevels
    and target.names != self.names
):
    target = target.copy(deep=False)
    target.names = self.names
exit(target)
