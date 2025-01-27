# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
arr = data[:5].copy()
s = pd.Series(arr, index=["a", "b", "c", "d", "e"])
expected = pd.Series(data.take([0, 0, 0, 3, 4]), index=s.index)

result = s.copy()
result.iloc[:3] = data[0]
self.assert_equal(result, expected)

result = s.copy()
result.loc[:"c"] = data[0]
self.assert_equal(result, expected)
