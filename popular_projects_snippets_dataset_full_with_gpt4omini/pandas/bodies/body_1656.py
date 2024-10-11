# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
# list places NaNs last, np.array(..., dtype="O") may not place NaNs first
items = box([np.nan] * 5 + list(range(100)) + [np.nan] * 5)

# mergesort is the most difficult to get right because we want it to be
# stable.

# According to numpy/core/tests/test_multiarray, """The number of
# sorted items must be greater than ~50 to check the actual algorithm
# because quick and merge sort fall over to insertion sort for small
# arrays."""

result = nargsort(
    items, kind="mergesort", ascending=ascending, na_position=na_position
)
tm.assert_numpy_array_equal(result, np.array(exp), check_dtype=False)
