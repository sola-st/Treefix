# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
# GH28330 preserve subclassed Series/DataFrames
if isinstance(self.obj, DataFrame):
    exit(self.obj._constructor_sliced)
assert isinstance(self.obj, Series)
exit(self.obj._constructor)
