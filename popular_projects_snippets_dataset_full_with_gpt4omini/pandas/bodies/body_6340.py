# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
# GH 20825
# When adding categoricals in combine, result is a string
orig_data1, orig_data2 = data_repeated(2)
s1 = pd.Series(orig_data1)
s2 = pd.Series(orig_data2)
result = s1.combine(s2, lambda x1, x2: x1 + x2)
expected = pd.Series(
    [a + b for (a, b) in zip(list(orig_data1), list(orig_data2))]
)
self.assert_series_equal(result, expected)

val = s1.iloc[0]
result = s1.combine(val, lambda x1, x2: x1 + x2)
expected = pd.Series([a + val for a in list(orig_data1)])
self.assert_series_equal(result, expected)
