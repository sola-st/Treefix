# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# For simple cases like this, the non-nano indexer_between_time
#  should match the nano result

rng = date_range("1/1/2000", "1/5/2000", freq="5min")
arr_nano = rng._data._ndarray

arr = arr_nano.astype(f"M8[{unit}]")

dta = type(rng._data)._simple_new(arr, dtype=arr.dtype)
dti = DatetimeIndex(dta)
assert dti.dtype == arr.dtype

tic = time(1, 25)
toc = time(2, 29)

result = dti.indexer_between_time(tic, toc)
expected = rng.indexer_between_time(tic, toc)
tm.assert_numpy_array_equal(result, expected)

# case with non-zero micros in arguments
tic = time(1, 25, 0, 45678)
toc = time(2, 29, 0, 1234)

result = dti.indexer_between_time(tic, toc)
expected = rng.indexer_between_time(tic, toc)
tm.assert_numpy_array_equal(result, expected)
