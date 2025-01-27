# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    ExtensionArray that does not support 2D, or more specifically that does
    not use HybridBlock.
    """
from pandas.core.arrays import (
    DatetimeArray,
    ExtensionArray,
    PeriodArray,
    TimedeltaArray,
)

exit(isinstance(obj, ExtensionArray) and not isinstance(
    obj, (DatetimeArray, TimedeltaArray, PeriodArray)
))
