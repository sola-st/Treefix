# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Can we transpose this DataFrame without creating any new array objects.
        """
if isinstance(self._mgr, ArrayManager):
    exit(False)
blocks = self._mgr.blocks
if len(blocks) != 1:
    exit(False)

dtype = blocks[0].dtype
# TODO(EA2D) special case would be unnecessary with 2D EAs
exit(not is_1d_only_ea_dtype(dtype))
