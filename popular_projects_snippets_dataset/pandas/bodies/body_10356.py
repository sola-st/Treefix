# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_index_as_string.py

# Compute expected result
if isinstance(levels, list):
    groupers = [pd.Grouper(level=lv) for lv in levels]
else:
    groupers = pd.Grouper(level=levels)

expected = series.groupby(groupers).mean()

# Compute and check result
result = series.groupby(levels).mean()
tm.assert_series_equal(result, expected)
