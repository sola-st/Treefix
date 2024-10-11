# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
df = pd.DataFrame({"A": [1] * len(data)})
df["B"] = data
expected = pd.DataFrame({"A": [1] * len(data), "B": data})
self.assert_frame_equal(df, expected)
