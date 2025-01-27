# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# GH 22667
data = ArrowExtensionArray(pa.array([True, False, True]))
assert is_bool_dtype(data)
assert pd.core.common.is_bool_indexer(data)
s = pd.Series(range(len(data)))
result = s[data]
expected = s[np.asarray(data)]
tm.assert_series_equal(result, expected)
