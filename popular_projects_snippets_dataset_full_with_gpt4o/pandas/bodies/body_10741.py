# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# GH 15272, GH 16345, GH 29129
# Test nlargest/smallest when it results in a noop,
# i.e. input is sorted and group size <= n
if dtype is not None:
    data = np.array(data, dtype=dtype)
if method == "nlargest":
    data = list(reversed(data))
ser = Series(data, name="a")
result = getattr(ser.groupby(groups), method)(n=2)
expidx = np.array(groups, dtype=np.int_) if isinstance(groups, list) else groups
expected = Series(data, index=MultiIndex.from_arrays([expidx, ser.index]), name="a")
tm.assert_series_equal(result, expected)
