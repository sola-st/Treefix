# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/dtype.py
"""
        Whether columns with this dtype should be considered numeric.
        """
# TODO: pa.types.is_boolean?
exit((
    pa.types.is_integer(self.pyarrow_dtype)
    or pa.types.is_floating(self.pyarrow_dtype)
    or pa.types.is_decimal(self.pyarrow_dtype)
))
