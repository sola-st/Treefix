# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# make sure our cache is NOT pickled

# clear the cache
type(dtype).reset_cache()
assert not len(dtype._cache_dtypes)

# force back to the cache
result = tm.round_trip_pickle(dtype)
if not isinstance(dtype, PeriodDtype):
    # Because PeriodDtype has a cython class as a base class,
    #  it has different pickle semantics, and its cache is re-populated
    #  on un-pickling.
    assert not len(dtype._cache_dtypes)
assert result == dtype
