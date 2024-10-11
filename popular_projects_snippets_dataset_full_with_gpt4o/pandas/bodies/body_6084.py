# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# https://github.com/pandas-dev/pandas/issues/31503
mask = pd.array(np.zeros(data.shape, dtype="bool"), dtype="boolean")
mask[:2] = pd.NA
mask[2:4] = True

result = data[mask]
expected = data[mask.fillna(False)]

self.assert_extension_array_equal(result, expected)

s = pd.Series(data)

result = s[mask]
expected = s[mask.fillna(False)]

self.assert_series_equal(result, expected)
