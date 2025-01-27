# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
df = pd.DataFrame({"A": data})
df["B"] = [1] * len(data)
expected = pd.DataFrame({"A": data, "B": [1] * len(data)})
self.assert_frame_equal(df, expected)
