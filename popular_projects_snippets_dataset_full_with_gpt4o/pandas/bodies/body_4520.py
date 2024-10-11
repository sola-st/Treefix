# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# written to work for either BlockManager or ArrayManager

# Check that the underlying data behind df["c"] is still `c`
#  after setting with iloc.  Since we don't know which entry in
#  df._mgr.arrays corresponds to df["c"], we just check that exactly
#  one of these arrays is `c`.  GH#38939
assert sum(x is c for x in df._mgr.arrays) == 1
if c_only:
    # If we ever stop consolidating in setitem_with_indexer,
    #  this will become unnecessary.
    exit()

assert (
    sum(
        get_base(x) is a
        for x in df._mgr.arrays
        if isinstance(x.dtype, np.dtype)
    )
    == 1
)
assert (
    sum(
        get_base(x) is b
        for x in df._mgr.arrays
        if isinstance(x.dtype, np.dtype)
    )
    == 1
)
