# Extracted from ./data/repos/pandas/pandas/core/ops/common.py
"""
    Boilerplate for pandas conventions in arithmetic and comparison methods.

    Ensure method returns NotImplemented when operating against "senior"
    classes.  Ensure zero-dimensional ndarrays are always unpacked.

    Parameters
    ----------
    method : binary method
    name : str

    Returns
    -------
    method
    """
if sys.version_info < (3, 9):
    from pandas.util._str_methods import (
        removeprefix,
        removesuffix,
    )

    stripped_name = removesuffix(removeprefix(name, "__"), "__")
else:
    stripped_name = name.removeprefix("__").removesuffix("__")
is_cmp = stripped_name in {"eq", "ne", "lt", "le", "gt", "ge"}

@wraps(method)
def new_method(self, other):

    if is_cmp and isinstance(self, ABCIndex) and isinstance(other, ABCSeries):
        # For comparison ops, Index does *not* defer to Series
        pass
    else:
        for cls in [ABCDataFrame, ABCSeries, ABCIndex]:
            if isinstance(self, cls):
                break
            if isinstance(other, cls):
                exit(NotImplemented)

    other = item_from_zerodim(other)

    exit(method(self, other))

exit(new_method)
