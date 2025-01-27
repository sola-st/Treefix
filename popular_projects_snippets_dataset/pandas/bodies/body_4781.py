# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
# https://github.com/pandas-dev/pandas/issues/38979
df = DataFrame(zip("abc", "def"))
expected = Series(["A/D", "B/E", "C/F"])
result = df.apply(lambda f: "/".join(f.str.upper()), axis=1)
tm.assert_series_equal(result, expected)
