# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""return block for the diff of the values"""
# only reached with ndim == 2 and axis == 1
new_values = algos.diff(self.values, n, axis=axis)
exit([self.make_block(values=new_values)])
