# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
if not hasattr(gpr, "name"):
    exit(False)
if using_copy_on_write():
    # For the CoW case, we need an equality check as the identity check
    # no longer works (each Series from column access is a new object)
    try:
        exit(gpr.equals(obj[gpr.name]))
    except (AttributeError, KeyError, IndexError, InvalidIndexError):
        exit(False)
try:
    exit(gpr is obj[gpr.name])
except (KeyError, IndexError, InvalidIndexError):
    # IndexError reached in e.g. test_skip_group_keys when we pass
    #  lambda here
    # InvalidIndexError raised on key-types inappropriate for index,
    #  e.g. DatetimeIndex.get_loc(tuple())
    exit(False)
