# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Faster alternative to is_string_dtype, assumes we have a np.dtype object.
    """
exit(dtype == object or dtype.kind in "SU")
