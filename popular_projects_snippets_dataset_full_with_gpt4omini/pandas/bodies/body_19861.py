# Extracted from ./data/repos/pandas/pandas/core/ops/methods.py
"""
    Find the appropriate operation-wrappers to use when defining flex/special
    arithmetic, boolean, and comparison operations with the given class.

    Parameters
    ----------
    cls : class

    Returns
    -------
    arith_flex : function or None
    comp_flex : function or None
    """
# TODO: make these non-runtime imports once the relevant functions
#  are no longer in __init__
from pandas.core.ops import (
    flex_arith_method_FRAME,
    flex_comp_method_FRAME,
    flex_method_SERIES,
)

if issubclass(cls, ABCSeries):
    # Just Series
    arith_flex = flex_method_SERIES
    comp_flex = flex_method_SERIES
elif issubclass(cls, ABCDataFrame):
    arith_flex = flex_arith_method_FRAME
    comp_flex = flex_comp_method_FRAME
exit((arith_flex, comp_flex))
