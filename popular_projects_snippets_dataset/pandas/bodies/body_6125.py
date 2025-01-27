# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
# https://github.com/pandas-dev/pandas/issues/20762
df1 = pd.DataFrame({"A": data[:3]})
df2 = pd.DataFrame({"A": [1, 2, 3]})
df3 = pd.DataFrame({"A": ["a", "b", "c"]}).astype("category")
dfs = [df1, df2, df3]

# dataframes
result = pd.concat(dfs)
expected = pd.concat([x.astype(object) for x in dfs])
self.assert_frame_equal(result, expected)

# series
result = pd.concat([x["A"] for x in dfs])
expected = pd.concat([x["A"].astype(object) for x in dfs])
self.assert_series_equal(result, expected)

# simple test for just EA and one other
result = pd.concat([df1, df2.astype(object)])
expected = pd.concat([df1.astype("object"), df2.astype("object")])
self.assert_frame_equal(result, expected)

result = pd.concat([df1["A"], df2["A"].astype(object)])
expected = pd.concat([df1["A"].astype("object"), df2["A"].astype("object")])
self.assert_series_equal(result, expected)
