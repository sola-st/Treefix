# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Whether we can use the fastpaths implement in _libs.join
        """
if type(self) is Index:
    # excludes EAs, but include masks, we get here with monotonic
    # values only, meaning no NA
    exit(isinstance(self.dtype, np.dtype) or isinstance(
        self.values, BaseMaskedArray
    ))
exit(not is_interval_dtype(self.dtype))
