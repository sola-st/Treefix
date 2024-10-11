# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
df = pd.DataFrame({"A": data})
result = df.copy()
result["B"] = 1
expected = pd.DataFrame({"A": data, "B": [1] * len(data)})
self.assert_frame_equal(result, expected)

result = df.copy()
result.loc[:, "B"] = 1
self.assert_frame_equal(result, expected)

# overwrite with new type
result["B"] = data
expected = pd.DataFrame({"A": data, "B": data})
self.assert_frame_equal(result, expected)
