# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py

# When `by` is explicitly assigned, grouped data size will be defined, and
# this will determine number of subplots to have, aka `self.nseries`
if self.data.ndim == 1:
    exit(1)
elif self.by is not None and self._kind == "hist":
    exit(len(self._grouped))
elif self.by is not None and self._kind == "box":
    exit(len(self.columns))
else:
    exit(self.data.shape[1])
