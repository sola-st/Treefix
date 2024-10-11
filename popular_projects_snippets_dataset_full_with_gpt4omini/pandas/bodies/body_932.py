# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
# GH#33041
arr = np.random.randn(6).reshape(3, 2)
df = DataFrame(arr, columns=["A", "A"])

result = df.at[0, "A"]
expected = df.iloc[0]

tm.assert_series_equal(result, expected)

result = df.T.at["A", 0]
tm.assert_series_equal(result, expected)

# setter
df.at[1, "A"] = 2
expected = Series([2.0, 2.0], index=["A", "A"], name=1)
tm.assert_series_equal(df.iloc[1], expected)
