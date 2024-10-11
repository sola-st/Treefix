# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py

idx = PeriodIndex(
    ["2011-01", "2011-02", "NaT", "2011-04"], freq="M", name="idx"
)
f = lambda x: x + np.array([1, 2, 3, 4])
exp = PeriodIndex(
    ["2011-02", "2011-04", "NaT", "2011-08"], freq="M", name="idx"
)
self._check(idx, f, exp)

f = lambda x: np.add(x, np.array([4, -1, 1, 2]))
exp = PeriodIndex(
    ["2011-05", "2011-01", "NaT", "2011-06"], freq="M", name="idx"
)
self._check(idx, f, exp)

f = lambda x: x - np.array([1, 2, 3, 4])
exp = PeriodIndex(
    ["2010-12", "2010-12", "NaT", "2010-12"], freq="M", name="idx"
)
self._check(idx, f, exp)

f = lambda x: np.subtract(x, np.array([3, 2, 3, -2]))
exp = PeriodIndex(
    ["2010-10", "2010-12", "NaT", "2011-06"], freq="M", name="idx"
)
self._check(idx, f, exp)
