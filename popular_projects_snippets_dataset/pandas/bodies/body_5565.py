# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
obj = index_or_series_obj
with tm.maybe_produces_warning(
    PerformanceWarning,
    sort
    and pa_version_under7p0
    and getattr(obj.dtype, "storage", "") == "pyarrow",
):
    result_codes, result_uniques = obj.factorize(sort=sort)

constructor = Index
if isinstance(obj, MultiIndex):
    constructor = MultiIndex.from_tuples
expected_arr = obj.unique()
if expected_arr.dtype == np.float16:
    expected_arr = expected_arr.astype(np.float32)
expected_uniques = constructor(expected_arr)
if (
    isinstance(obj, Index)
    and expected_uniques.dtype == bool
    and obj.dtype == object
):
    expected_uniques = expected_uniques.astype(object)

if sort:
    with tm.maybe_produces_warning(
        PerformanceWarning,
        pa_version_under7p0 and getattr(obj.dtype, "storage", "") == "pyarrow",
    ):
        expected_uniques = expected_uniques.sort_values()

        # construct an integer ndarray so that
        # `expected_uniques.take(expected_codes)` is equal to `obj`
expected_uniques_list = list(expected_uniques)
expected_codes = [expected_uniques_list.index(val) for val in obj]
expected_codes = np.asarray(expected_codes, dtype=np.intp)

tm.assert_numpy_array_equal(result_codes, expected_codes)
tm.assert_index_equal(result_uniques, expected_uniques, exact=True)
