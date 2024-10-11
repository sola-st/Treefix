# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
idx = PeriodIndex(
    ["2011-01", "2011-02", "2011-03", "2011-04"], freq="M", name="idx"
)

expected = PeriodIndex(
    ["2011-03", "2011-04", "2011-05", "2011-06"], freq="M", name="idx"
)

self._check(idx, lambda x: x + 2, expected)
self._check(idx, lambda x: 2 + x, expected)

self._check(idx + 2, lambda x: x - 2, idx)

result = idx - Period("2011-01", freq="M")
off = idx.freq
exp = pd.Index([0 * off, 1 * off, 2 * off, 3 * off], name="idx")
tm.assert_index_equal(result, exp)

result = Period("2011-01", freq="M") - idx
exp = pd.Index([0 * off, -1 * off, -2 * off, -3 * off], name="idx")
tm.assert_index_equal(result, exp)
