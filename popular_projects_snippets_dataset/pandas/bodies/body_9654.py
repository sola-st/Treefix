# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked_shared.py
# The base class casts to object dtype, for which searchsorted returns
#  0 from the left and 10 from the right.
arr = pd.array(range(10), dtype=dtype)

assert arr.searchsorted(np.nan, side="left") == 10
assert arr.searchsorted(np.nan, side="right") == 10
