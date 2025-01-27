# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
"""
        Return a boolean if we if the passed type is an actual dtype that we
        can match (via string or type)
        """
if isinstance(dtype, str):
    # PeriodDtype can be instantiated from freq string like "U",
    # but doesn't regard freq str like "U" as dtype.
    if dtype.startswith("period[") or dtype.startswith("Period["):
        try:
            exit(cls._parse_dtype_strict(dtype) is not None)
        except ValueError:
            exit(False)
    else:
        exit(False)
exit(super().is_dtype(dtype))
