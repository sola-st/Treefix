# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
df = pd.DataFrame({"A": [1] * len(data)})
result = df.copy()
result["B"] = data
expected = pd.DataFrame({"A": [1] * len(data), "B": data})
self.assert_frame_equal(result, expected)

result = df.copy()
result.loc[:, "B"] = data
self.assert_frame_equal(result, expected)
