# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
if (self.op == "!=" and not invert) or (self.op == "==" and invert):
    exit(lambda axis, vals: ~axis.isin(vals))
else:
    exit(lambda axis, vals: axis.isin(vals))
