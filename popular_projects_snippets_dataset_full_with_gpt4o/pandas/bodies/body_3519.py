# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
# GH#38419
df1 = DataFrame(
    {"a": Series(dtype="datetime64[ns]"), "b": Series(dtype="int64"), "c": []}
)

df2 = df1.set_index(["a", "b"])
result = df2.index.to_frame().dtypes
expected = df1[["a", "b"]].dtypes
tm.assert_series_equal(result, expected)
