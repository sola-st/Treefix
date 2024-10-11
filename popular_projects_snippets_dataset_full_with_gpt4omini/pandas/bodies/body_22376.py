# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
        Helper function to determine if dtype is valid for
        nsmallest/nlargest methods
        """
exit((
    is_numeric_dtype(dtype) and not is_complex_dtype(dtype)
) or needs_i8_conversion(dtype))
