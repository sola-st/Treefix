# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# GH 20882
s = pd.Series(data, index=[2 * i for i in range(len(data))])
assert s.get(4) == s.iloc[2]

result = s.get([4, 6])
expected = s.iloc[[2, 3]]
self.assert_series_equal(result, expected)

result = s.get(slice(2))
expected = s.iloc[[0, 1]]
self.assert_series_equal(result, expected)

assert s.get(-1) is None
assert s.get(s.index.max() + 1) is None

s = pd.Series(data[:6], index=list("abcdef"))
assert s.get("c") == s.iloc[2]

result = s.get(slice("b", "d"))
expected = s.iloc[[1, 2, 3]]
self.assert_series_equal(result, expected)

result = s.get("Z")
assert result is None

assert s.get(4) == s.iloc[4]
assert s.get(-1) == s.iloc[-1]
assert s.get(len(s)) is None

# GH 21257
s = pd.Series(data)
with tm.assert_produces_warning(None):
    # GH#45324 make sure we aren't giving a spurious FutureWarning
    s2 = s[::2]
assert s2.get(1) is None
