# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        raise if this Index subclass does not support any or all.
        """
if (
    isinstance(self, ABCMultiIndex)
    or needs_i8_conversion(self.dtype)
    or is_interval_dtype(self.dtype)
    or is_categorical_dtype(self.dtype)
    or is_float_dtype(self.dtype)
):
    # This call will raise
    make_invalid_op(opname)(self)
