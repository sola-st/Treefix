# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# all numeric columns -> numeric series
df = DataFrame(
    {
        "A": pd.array([1, 2], dtype="Int64"),
        "B": np.array([1, 2], dtype="int64"),
    },
    index=["a", "b"],
)
result = df.loc["a"]
expected = Series([1, 1], dtype="Int64", index=["A", "B"], name="a")
tm.assert_series_equal(result, expected)

result = df.iloc[0]
tm.assert_series_equal(result, expected)

# mixed columns -> object series
df = DataFrame(
    {"A": pd.array([1, 2], dtype="Int64"), "B": np.array(["a", "b"])},
    index=["a", "b"],
)
result = df.loc["a"]
expected = Series([1, "a"], dtype=object, index=["A", "B"], name="a")
tm.assert_series_equal(result, expected)

result = df.iloc[0]
tm.assert_series_equal(result, expected)
