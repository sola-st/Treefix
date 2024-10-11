# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
grouped = ts.groupby(lambda x: x.month, group_keys=False)
result = grouped.apply(lambda x: x * 2)
expected = grouped.transform(lambda x: x * 2)
tm.assert_series_equal(result, expected)
