# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
box = index_or_series_or_array

with tm.assert_produces_warning(None):
    thing = box(arr)

if arr.dtype.name == "int64" and box is pd.array:
    mark = pytest.mark.xfail(reason="thing is Int64 and to_numpy() returns object")
    request.node.add_marker(mark)

result = thing.to_numpy()
tm.assert_numpy_array_equal(result, expected)

result = np.asarray(thing)
tm.assert_numpy_array_equal(result, expected)
