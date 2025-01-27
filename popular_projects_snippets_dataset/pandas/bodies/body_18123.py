# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
idx = PeriodIndex(
    ["2011-01", "2011-02", "2011-03", "2011-04"], freq="M", name="idx"
)
per = idx[2]

f = lambda x: x == per
exp = np.array([False, False, True, False], dtype=np.bool_)
self._check(idx, f, exp)
f = lambda x: per == x
self._check(idx, f, exp)

f = lambda x: x != per
exp = np.array([True, True, False, True], dtype=np.bool_)
self._check(idx, f, exp)
f = lambda x: per != x
self._check(idx, f, exp)

f = lambda x: per >= x
exp = np.array([True, True, True, False], dtype=np.bool_)
self._check(idx, f, exp)

f = lambda x: x > per
exp = np.array([False, False, False, True], dtype=np.bool_)
self._check(idx, f, exp)

f = lambda x: per >= x
exp = np.array([True, True, True, False], dtype=np.bool_)
self._check(idx, f, exp)
