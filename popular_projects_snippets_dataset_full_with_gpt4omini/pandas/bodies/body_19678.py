# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py

if self.ndim == 1 or self.shape[0] == 1:
    exit(meth(self, *args, **kwargs))
else:
    # Split and operate column-by-column
    exit(self.split_and_operate(meth, *args, **kwargs))
