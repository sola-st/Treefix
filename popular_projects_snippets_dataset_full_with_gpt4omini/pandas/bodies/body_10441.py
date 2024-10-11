# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 17093
if reduction_func == "corrwith":
    msg = "corrwith not implemented for SeriesGroupBy"
    request.node.add_marker(pytest.mark.xfail(reason=msg))

# GH 17093
index = [1, 2, 3, 4]  # test transform preserves non-standard index
ser = Series([1, 2, 2, 3], index=index)
gb = ser.groupby([1, 1, np.nan, np.nan], dropna=dropna)

args = get_groupby_method_args(reduction_func, ser)

# Manually handle reducers that don't fit the generic pattern
# Set expected with dropna=False, then replace if necessary
if reduction_func == "first":
    expected = Series([1, 1, 2, 2], index=index)
elif reduction_func == "last":
    expected = Series([2, 2, 3, 3], index=index)
elif reduction_func == "nth":
    expected = Series([1, 1, 2, 2], index=index)
elif reduction_func == "size":
    expected = Series([2, 2, 2, 2], index=index)
elif reduction_func == "corrwith":
    expected = Series([1, 1, 2, 2], index=index)
else:
    expected_gb = ser.groupby([1, 1, np.nan, np.nan], dropna=False)
    buffer = []
    for idx, group in expected_gb:
        res = getattr(group, reduction_func)()
        buffer.append(Series(res, index=group.index))
    expected = concat(buffer)
if dropna:
    dtype = object if reduction_func in ("any", "all") else float
    expected = expected.astype(dtype)
    expected.iloc[[2, 3]] = np.nan

result = gb.transform(reduction_func, *args)
tm.assert_series_equal(result, expected)
