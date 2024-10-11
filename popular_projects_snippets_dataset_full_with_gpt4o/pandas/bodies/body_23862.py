# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""set the data for this column"""
setattr(self.attrs, self.kind_attr, self.values)
setattr(self.attrs, self.meta_attr, self.meta)
assert self.dtype is not None
setattr(self.attrs, self.dtype_attr, self.dtype)
