# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# GH-17569
cat_idx = CategoricalIndex(idx_values, ordered=ordered)
df = DataFrame({"A": ["foo", "bar", "baz"]}, index=cat_idx)
sl = slice(idx_values[0], idx_values[1])

# scalar selection
result = df.loc[idx_values[0]]
expected = Series(["foo"], index=["A"], name=idx_values[0])
tm.assert_series_equal(result, expected)

# list selection
result = df.loc[idx_values[:2]]
expected = DataFrame(["foo", "bar"], index=cat_idx[:2], columns=["A"])
tm.assert_frame_equal(result, expected)

# slice selection
result = df.loc[sl]
expected = DataFrame(["foo", "bar"], index=cat_idx[:2], columns=["A"])
tm.assert_frame_equal(result, expected)

# scalar assignment
result = df.copy()
result.loc[idx_values[0]] = "qux"
expected = DataFrame({"A": ["qux", "bar", "baz"]}, index=cat_idx)
tm.assert_frame_equal(result, expected)

# list assignment
result = df.copy()
result.loc[idx_values[:2], "A"] = ["qux", "qux2"]
expected = DataFrame({"A": ["qux", "qux2", "baz"]}, index=cat_idx)
tm.assert_frame_equal(result, expected)

# slice assignment
result = df.copy()
result.loc[sl, "A"] = ["qux", "qux2"]
expected = DataFrame({"A": ["qux", "qux2", "baz"]}, index=cat_idx)
tm.assert_frame_equal(result, expected)
