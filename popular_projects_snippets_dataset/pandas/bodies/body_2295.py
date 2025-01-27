# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# upcasting case (GH # 2794)
df = DataFrame(
    {
        c: Series([1] * 3, dtype=c)
        for c in ["float32", "float64", "int32", "int64"]
    }
)
df.iloc[1, :] = 0
result = df.dtypes
expected = Series(
    [
        np.dtype("float32"),
        np.dtype("float64"),
        np.dtype("int32"),
        np.dtype("int64"),
    ],
    index=["float32", "float64", "int32", "int64"],
)

# when we don't preserve boolean casts
#
# expected = Series({ 'float32' : 1, 'float64' : 3 })

tm.assert_series_equal(result, expected)
