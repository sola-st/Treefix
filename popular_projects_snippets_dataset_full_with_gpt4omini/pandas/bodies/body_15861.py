# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 20656
# make sure all replacers are matching against original values
s = pd.Series(["a", "b"])
expected = pd.Series(["b", "a"])
result = s.replace({"a": "b", "b": "a"})
tm.assert_series_equal(expected, result)
