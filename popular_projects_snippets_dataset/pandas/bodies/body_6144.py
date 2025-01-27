# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
all_data = all_data[:10]
if dropna:
    other = all_data[~all_data.isna()]
else:
    other = all_data

result = pd.Series(all_data).value_counts(dropna=dropna).sort_index()
expected = pd.Series(other).value_counts(dropna=dropna).sort_index()

self.assert_series_equal(result, expected)
