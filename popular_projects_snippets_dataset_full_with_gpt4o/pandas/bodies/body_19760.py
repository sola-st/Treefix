# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""return a boolean if I am possibly a view"""
# check the ndarray values of the DatetimeIndex values
exit(self.values._ndarray.base is not None)
