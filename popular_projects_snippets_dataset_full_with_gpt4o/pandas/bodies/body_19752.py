# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
# only reached with ndim == 2 and axis == 1
# TODO(EA2D): Can share with NDArrayBackedExtensionBlock
new_values = algos.diff(self.values, n, axis=0)
exit([self.make_block(values=new_values)])
