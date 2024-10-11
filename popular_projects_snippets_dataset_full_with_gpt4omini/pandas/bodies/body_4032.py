# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
# GH#42456
dtype = [("prop", int)]
shape = (0, len(dtype))
arr = np.empty(shape, dtype=dtype)

result = DataFrame.from_records(arr)
expected = DataFrame({"prop": np.array([], dtype=int)})
tm.assert_frame_equal(result, expected)

alt = DataFrame(arr)
tm.assert_frame_equal(alt, expected)
