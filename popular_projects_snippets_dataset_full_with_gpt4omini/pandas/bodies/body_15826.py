# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
if dtype == "float64[pyarrow]":
    if method == "average":
        exp_dtype = "float64[pyarrow]"
    else:
        exp_dtype = "uint64[pyarrow]"
else:
    exp_dtype = "float64"

chunk = 3
in_arr = [neg_inf] * chunk + [na_value] * chunk + [pos_inf] * chunk
iseries = Series(in_arr, dtype=dtype)
exp_ranks = {
    "average": ([2, 2, 2], [5, 5, 5], [8, 8, 8]),
    "min": ([1, 1, 1], [4, 4, 4], [7, 7, 7]),
    "max": ([3, 3, 3], [6, 6, 6], [9, 9, 9]),
    "first": ([1, 2, 3], [4, 5, 6], [7, 8, 9]),
    "dense": ([1, 1, 1], [2, 2, 2], [3, 3, 3]),
}
ranks = exp_ranks[method]
if na_option == "top":
    order = [ranks[1], ranks[0], ranks[2]]
elif na_option == "bottom":
    order = [ranks[0], ranks[2], ranks[1]]
else:
    order = [ranks[0], [np.nan] * chunk, ranks[1]]
expected = order if ascending else order[::-1]
expected = list(chain.from_iterable(expected))
result = iseries.rank(method=method, na_option=na_option, ascending=ascending)
tm.assert_series_equal(result, Series(expected, dtype=exp_dtype))
