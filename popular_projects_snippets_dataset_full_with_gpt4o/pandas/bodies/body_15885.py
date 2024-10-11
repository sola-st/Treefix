# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH-48644
series = pd.Series(["0"])
expected = pd.Series([1])
result = series.replace(to_replace="0", value=1, regex=regex)
tm.assert_series_equal(result, expected)
