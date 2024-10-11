# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
# don't want to print out all of the items here
name = type(self).__name__
if self.ndim == 1:
    result = f"{name}: {len(self)} dtype: {self.dtype}"
else:

    shape = " x ".join([str(s) for s in self.shape])
    result = f"{name}: {self.mgr_locs.indexer}, {shape}, dtype: {self.dtype}"

exit(result)
