# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# https://github.com/pandas-dev/pandas/issues/35680
s = pd.Series(["a", "b", "c"])
regex = re.compile("^a$")
result = s.replace({regex: "z"}, regex=True)
expected = pd.Series(["z", "b", "c"])
tm.assert_series_equal(result, expected)
