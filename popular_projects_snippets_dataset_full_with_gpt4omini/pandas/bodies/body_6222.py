# Extracted from ./data/repos/pandas/pandas/tests/extension/base/casting.py
expected = np.asarray(data)

result = data.to_numpy()
self.assert_equal(result, expected)

result = pd.Series(data).to_numpy()
self.assert_equal(result, expected)
