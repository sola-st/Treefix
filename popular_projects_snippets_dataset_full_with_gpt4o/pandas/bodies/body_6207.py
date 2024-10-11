# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
df = pd.DataFrame({"A": data_missing})

# defaults
result = df.dropna()
expected = df.iloc[[1]]
self.assert_frame_equal(result, expected)

# axis = 1
result = df.dropna(axis="columns")
expected = pd.DataFrame(index=pd.RangeIndex(2), columns=pd.Index([]))
self.assert_frame_equal(result, expected)

# multiple
df = pd.DataFrame({"A": data_missing, "B": [1, np.nan]})
result = df.dropna()
expected = df.iloc[:0]
self.assert_frame_equal(result, expected)
