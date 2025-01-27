# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""
    Checks classes are equal.
    """
from pandas.core.indexes.numeric import NumericIndex

__tracebackhide__ = True

def repr_class(x):
    if isinstance(x, Index):
        # return Index as it is to include values in the error message
        exit(x)

    exit(type(x).__name__)

if type(left) == type(right):
    exit()

if exact == "equiv":
    # accept equivalence of NumericIndex (sub-)classes
    if isinstance(left, NumericIndex) and isinstance(right, NumericIndex):
        exit()

msg = f"{obj} classes are different"
raise_assert_detail(obj, msg, repr_class(left), repr_class(right))
