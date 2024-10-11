# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py

n = 4
kwargs = {
    frame_or_series._get_axis_name(i): list(range(n))
    for i in range(frame_or_series._AXIS_LEN)
}

# get the numeric data
o = construct(frame_or_series, n, **kwargs)
result = o._get_numeric_data()
tm.assert_equal(result, o)

# non-inclusion
result = o._get_bool_data()
expected = construct(frame_or_series, n, value="empty", **kwargs)
if isinstance(o, DataFrame):
    # preserve columns dtype
    expected.columns = o.columns[:0]
# https://github.com/pandas-dev/pandas/issues/50862
tm.assert_equal(result.reset_index(drop=True), expected)

# get the bool data
arr = np.array([True, True, False, True])
o = construct(frame_or_series, n, value=arr, **kwargs)
result = o._get_numeric_data()
tm.assert_equal(result, o)
