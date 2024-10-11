# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# GH6394
# Regression in chained getitem indexing with embedded list-like from
# 0.12

df = DataFrame({"A": 5 * [np.zeros(3)], "B": 5 * [np.ones(3)]})
expected = df["A"].iloc[2]
result = df.loc[2, "A"]
tm.assert_numpy_array_equal(result, expected)
result2 = df.iloc[2]["A"]
tm.assert_numpy_array_equal(result2, expected)
result3 = df["A"].loc[2]
tm.assert_numpy_array_equal(result3, expected)
result4 = df["A"].iloc[2]
tm.assert_numpy_array_equal(result4, expected)
