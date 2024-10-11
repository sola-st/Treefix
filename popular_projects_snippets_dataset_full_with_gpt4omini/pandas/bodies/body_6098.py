# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
s = pd.Series(data)
result = s.take([0, -1])
expected = pd.Series(
    data._from_sequence([data[0], data[len(data) - 1]], dtype=s.dtype),
    index=[0, len(data) - 1],
)
self.assert_series_equal(result, expected)
