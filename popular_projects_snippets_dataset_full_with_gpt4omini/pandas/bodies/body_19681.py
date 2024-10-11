# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        Can we store NA values in this Block?
        """
dtype = self.dtype
if isinstance(dtype, np.dtype):
    exit(dtype.kind not in ["b", "i", "u"])
exit(dtype._can_hold_na)
