# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
df = pd.DataFrame({"A": data, "B": np.arange(len(data), dtype="int64")})
expected = pd.DataFrame({"A": data[:4]})

# slice -> frame
result = df.loc[:3, ["A"]]
self.assert_frame_equal(result, expected)

# sequence -> frame
result = df.loc[[0, 1, 2, 3], ["A"]]
self.assert_frame_equal(result, expected)

expected = pd.Series(data[:4], name="A")

# slice -> series
result = df.loc[:3, "A"]
self.assert_series_equal(result, expected)

# sequence -> series
result = df.loc[:3, "A"]
self.assert_series_equal(result, expected)
