# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
dti = pd.date_range("2016-01-01", periods=3, freq="QS")
pi = dti.to_period("Q")

cond = np.array([False, True, False])

# Passing a valid scalar
value = pi[-1] + pi.freq * 10
expected = pd.PeriodIndex([value, pi[1], value])
result = pi.where(cond, value)
tm.assert_index_equal(result, expected)

# Case passing ndarray[object] of Periods
other = np.asarray(pi + pi.freq * 10, dtype=object)
result = pi.where(cond, other)
expected = pd.PeriodIndex([other[0], pi[1], other[2]])
tm.assert_index_equal(result, expected)

# Passing a mismatched scalar -> casts to object
td = pd.Timedelta(days=4)
expected = pd.Index([td, pi[1], td], dtype=object)
result = pi.where(cond, td)
tm.assert_index_equal(result, expected)

per = pd.Period("2020-04-21", "D")
expected = pd.Index([per, pi[1], per], dtype=object)
result = pi.where(cond, per)
tm.assert_index_equal(result, expected)
