# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# test list of lists/ndarrays
df = DataFrame([np.arange(5) for x in range(5)])
result = df.dtypes
expected = Series([np.dtype("int")] * 5)
tm.assert_series_equal(result, expected)

df = DataFrame([np.array(np.arange(5), dtype="int32") for x in range(5)])
result = df.dtypes
expected = Series([np.dtype("int32")] * 5)
tm.assert_series_equal(result, expected)

# overflow issue? (we always expected int64 upcasting here)
df = DataFrame({"a": [2**31, 2**31 + 1]})
assert df.dtypes.iloc[0] == np.dtype("int64")

# GH #2751 (construction with no index specified), make sure we cast to
# platform values
df = DataFrame([1, 2])
assert df.dtypes.iloc[0] == np.dtype("int64")

df = DataFrame([1.0, 2.0])
assert df.dtypes.iloc[0] == np.dtype("float64")

df = DataFrame({"a": [1, 2]})
assert df.dtypes.iloc[0] == np.dtype("int64")

df = DataFrame({"a": [1.0, 2.0]})
assert df.dtypes.iloc[0] == np.dtype("float64")

df = DataFrame({"a": 1}, index=range(3))
assert df.dtypes.iloc[0] == np.dtype("int64")

df = DataFrame({"a": 1.0}, index=range(3))
assert df.dtypes.iloc[0] == np.dtype("float64")

# with object list
df = DataFrame(
    {
        "a": [1, 2, 4, 7],
        "b": [1.2, 2.3, 5.1, 6.3],
        "c": list("abcd"),
        "d": [datetime(2000, 1, 1) for i in range(4)],
        "e": [1.0, 2, 4.0, 7],
    }
)
result = df.dtypes
expected = Series(
    [
        np.dtype("int64"),
        np.dtype("float64"),
        np.dtype("object"),
        np.dtype("datetime64[ns]"),
        np.dtype("float64"),
    ],
    index=list("abcde"),
)
tm.assert_series_equal(result, expected)
