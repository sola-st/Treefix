# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
df = pd.DataFrame({"A": data, "B": np.arange(len(data), dtype="int64")})
expected = pd.DataFrame({"A": data[:4]})

# slice -> frame
result = df.iloc[:4, [0]]
self.assert_frame_equal(result, expected)

# sequence -> frame
result = df.iloc[[0, 1, 2, 3], [0]]
self.assert_frame_equal(result, expected)

expected = pd.Series(data[:4], name="A")

# slice -> series
result = df.iloc[:4, 0]
self.assert_series_equal(result, expected)

# sequence -> series
result = df.iloc[:4, 0]
self.assert_series_equal(result, expected)

# GH#32959 slice columns with step
result = df.iloc[:, ::2]
self.assert_frame_equal(result, df[["A"]])
result = df[["B", "A"]].iloc[:, ::2]
self.assert_frame_equal(result, df[["B"]])
