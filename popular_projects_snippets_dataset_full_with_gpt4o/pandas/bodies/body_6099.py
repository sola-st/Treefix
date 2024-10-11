# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
s = pd.Series(data)
result = s.reindex([0, 1, 3])
expected = pd.Series(data.take([0, 1, 3]), index=[0, 1, 3])
self.assert_series_equal(result, expected)

n = len(data)
result = s.reindex([-1, 0, n])
expected = pd.Series(
    data._from_sequence([na_value, data[0], na_value], dtype=s.dtype),
    index=[-1, 0, n],
)
self.assert_series_equal(result, expected)

result = s.reindex([n, n + 1])
expected = pd.Series(
    data._from_sequence([na_value, na_value], dtype=s.dtype), index=[n, n + 1]
)
self.assert_series_equal(result, expected)
