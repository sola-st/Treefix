# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py

# can convert dtypes
f = DataFrame(
    {
        "a": ["cat", "bat", "cat", "bat"],
        "v": [1, 2, 3, 4],
        "i": ["a", "b", "a", "b"],
    }
)
assert f.dtypes["v"] == "int64"

z = pivot_table(
    f, values="v", index=["a"], columns=["i"], fill_value=0, aggfunc=np.sum
)
result = z.dtypes
expected = Series([np.dtype("int64")] * 2, index=Index(list("ab"), name="i"))
tm.assert_series_equal(result, expected)

# cannot convert dtypes
f = DataFrame(
    {
        "a": ["cat", "bat", "cat", "bat"],
        "v": [1.5, 2.5, 3.5, 4.5],
        "i": ["a", "b", "a", "b"],
    }
)
assert f.dtypes["v"] == "float64"

z = pivot_table(
    f, values="v", index=["a"], columns=["i"], fill_value=0, aggfunc=np.mean
)
result = z.dtypes
expected = Series([np.dtype("float64")] * 2, index=Index(list("ab"), name="i"))
tm.assert_series_equal(result, expected)
