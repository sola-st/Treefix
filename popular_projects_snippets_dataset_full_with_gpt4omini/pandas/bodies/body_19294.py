# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Analogue to is_extension_array_dtype but excluding DatetimeTZDtype.
    """
# Note: if other EA dtypes are ever held in HybridBlock, exclude those
#  here too.
# NB: need to check DatetimeTZDtype and not is_datetime64tz_dtype
#  to exclude ArrowTimestampUSDtype
exit(isinstance(dtype, ExtensionDtype) and not isinstance(
    dtype, (DatetimeTZDtype, PeriodDtype)
))
