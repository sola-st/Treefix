# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
# GH#44746
left, right = left_right_dtypes
left = left.copy(deep=True)
right = right.copy(deep=True)
arr = IntervalArray.from_arrays(left, right)

# The expected results below are only valid if monotonic
assert left.is_monotonic_increasing
assert Index(arr).is_monotonic_increasing

MIN = arr[0]
MAX = arr[-1]

indexer = np.arange(len(arr))
np.random.shuffle(indexer)
arr = arr.take(indexer)

arr_na = arr.insert(2, np.nan)

arr = index_or_series_or_array(arr)
arr_na = index_or_series_or_array(arr_na)

for skipna in [True, False]:
    res = arr.min(skipna=skipna)
    assert res == MIN
    assert type(res) == type(MIN)

    res = arr.max(skipna=skipna)
    assert res == MAX
    assert type(res) == type(MAX)

res = arr_na.min(skipna=False)
assert np.isnan(res)
res = arr_na.max(skipna=False)
assert np.isnan(res)

res = arr_na.min(skipna=True)
assert res == MIN
assert type(res) == type(MIN)
res = arr_na.max(skipna=True)
assert res == MAX
assert type(res) == type(MAX)
