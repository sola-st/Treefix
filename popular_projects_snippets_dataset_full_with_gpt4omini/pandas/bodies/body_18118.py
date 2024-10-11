# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
idx1 = PeriodIndex(["2011-01", "2011-02", "NaT", "2011-05"], freq=freq)
per = idx1[1]

result = idx1 > per
exp = np.array([False, False, False, True])
tm.assert_numpy_array_equal(result, exp)
result = per < idx1
tm.assert_numpy_array_equal(result, exp)

result = idx1 == pd.NaT
exp = np.array([False, False, False, False])
tm.assert_numpy_array_equal(result, exp)
result = pd.NaT == idx1
tm.assert_numpy_array_equal(result, exp)

result = idx1 != pd.NaT
exp = np.array([True, True, True, True])
tm.assert_numpy_array_equal(result, exp)
result = pd.NaT != idx1
tm.assert_numpy_array_equal(result, exp)

idx2 = PeriodIndex(["2011-02", "2011-01", "2011-04", "NaT"], freq=freq)
result = idx1 < idx2
exp = np.array([True, False, False, False])
tm.assert_numpy_array_equal(result, exp)

result = idx1 == idx2
exp = np.array([False, False, False, False])
tm.assert_numpy_array_equal(result, exp)

result = idx1 != idx2
exp = np.array([True, True, True, True])
tm.assert_numpy_array_equal(result, exp)

result = idx1 == idx1
exp = np.array([True, True, False, True])
tm.assert_numpy_array_equal(result, exp)

result = idx1 != idx1
exp = np.array([False, False, True, False])
tm.assert_numpy_array_equal(result, exp)
