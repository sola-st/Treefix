# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#13200
base = PeriodIndex(["2011-01", "2011-02", "2011-03", "2011-04"], freq=freq)
base = tm.box_expected(base, box_with_array)

# TODO: could also box idx?
idx = PeriodIndex(["2011-02", "2011-01", "2011-03", "2011-05"], freq=freq)

xbox = get_upcast_box(base, idx, True)

exp = np.array([False, False, True, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base == idx, exp)

exp = np.array([True, True, False, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base != idx, exp)

exp = np.array([False, True, False, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base > idx, exp)

exp = np.array([True, False, False, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base < idx, exp)

exp = np.array([False, True, True, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base >= idx, exp)

exp = np.array([True, False, True, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base <= idx, exp)
