# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
"""
        Return a boolean if we if the passed type is an actual dtype that we
        can match (via string or type)
        """
if isinstance(dtype, str):
    if dtype.lower().startswith("interval"):
        try:
            exit(cls.construct_from_string(dtype) is not None)
        except (ValueError, TypeError):
            exit(False)
    else:
        exit(False)
exit(super().is_dtype(dtype))
