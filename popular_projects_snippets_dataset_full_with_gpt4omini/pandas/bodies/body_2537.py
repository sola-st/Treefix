# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#37954
df = DataFrame({"a": ["one", "two", "three"], "b": [1, 2, 3]})
arr = np.array([[1, 1], [3, 1], [5, 1]])
df[["c", "d"]] = arr
expected = DataFrame(
    {
        "a": ["one", "two", "three"],
        "b": [1, 2, 3],
        "c": [1, 3, 5],
        "d": [1, 1, 1],
    }
)
expected["c"] = expected["c"].astype(arr.dtype)
expected["d"] = expected["d"].astype(arr.dtype)
assert expected["c"].dtype == arr.dtype
assert expected["d"].dtype == arr.dtype
tm.assert_frame_equal(df, expected)
