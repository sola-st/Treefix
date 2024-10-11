# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# MultiIndex tested separately
index = index_flat
if not len(index):
    pytest.skip("Skip check for empty Index and MultiIndex")

idx = index[[0] * 5]
idx_unique = index[[0]]

# We test against `idx_unique`, so first we make sure it's unique
# and doesn't contain nans.
assert idx_unique.is_unique is True
try:
    assert idx_unique.hasnans is False
except NotImplementedError:
    pass

result = idx.unique()
tm.assert_index_equal(result, idx_unique)

# nans:
if not index._can_hold_na:
    pytest.skip("Skip na-check if index cannot hold na")

vals = index._values[[0] * 5]
vals[0] = np.nan

vals_unique = vals[:2]
idx_nan = index._shallow_copy(vals)
idx_unique_nan = index._shallow_copy(vals_unique)
assert idx_unique_nan.is_unique is True

assert idx_nan.dtype == index.dtype
assert idx_unique_nan.dtype == index.dtype

expected = idx_unique_nan
for pos, i in enumerate([idx_nan, idx_unique_nan]):
    result = i.unique()
    tm.assert_index_equal(result, expected)
