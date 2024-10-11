# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
arr = pd.array(["1", "2", "3"], dtype=dtype)
result = arr.astype("int64")
expected = np.array([1, 2, 3], dtype="int64")
tm.assert_numpy_array_equal(result, expected)

arr = pd.array(["1", pd.NA, "3"], dtype=dtype)
msg = r"int\(\) argument must be a string, a bytes-like object or a( real)? number"
with pytest.raises(TypeError, match=msg):
    arr.astype("int64")
