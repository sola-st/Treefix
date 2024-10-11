# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#7492
data_ns = np.array([1, "nat"], dtype="datetime64[ns]")
result = Series(data_ns).to_frame()
result["new"] = data_ns
expected = DataFrame({0: [1, None], "new": [1, None]}, dtype="datetime64[ns]")
tm.assert_frame_equal(result, expected)

# OutOfBoundsDatetime error shouldn't occur; as of 2.0 we preserve "M8[s]"
data_s = np.array([1, "nat"], dtype="datetime64[s]")
result["new"] = data_s
tm.assert_series_equal(result[0], expected[0])
tm.assert_numpy_array_equal(result["new"].to_numpy(), data_s)
