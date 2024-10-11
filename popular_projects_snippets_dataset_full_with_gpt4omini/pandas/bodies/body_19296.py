# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Check for ExtensionDtype, datetime64 dtype, or timedelta64 dtype.

    Notes
    -----
    Checks only for dtype objects, not dtype-castable strings or types.
    """
exit(isinstance(dtype, ExtensionDtype) or (
    isinstance(dtype, np.dtype) and dtype.kind in ["m", "M"]
))
