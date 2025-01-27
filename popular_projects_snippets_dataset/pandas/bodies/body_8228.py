# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_period.py
dti = date_range(start="1/1/2005", end="12/1/2005", freq="M")
pi1 = dti.to_period()
pi2 = dti.to_period(freq="D")
pi3 = dti.to_period(freq="3D")

assert pi1[0] == Period("Jan 2005", freq="M")
assert pi2[0] == Period("1/31/2005", freq="D")
assert pi3[0] == Period("1/31/2005", freq="3D")

assert pi1[-1] == Period("Nov 2005", freq="M")
assert pi2[-1] == Period("11/30/2005", freq="D")
assert pi3[-1], Period("11/30/2005", freq="3D")

tm.assert_index_equal(pi1, period_range("1/1/2005", "11/1/2005", freq="M"))
tm.assert_index_equal(
    pi2, period_range("1/1/2005", "11/1/2005", freq="M").asfreq("D")
)
tm.assert_index_equal(
    pi3, period_range("1/1/2005", "11/1/2005", freq="M").asfreq("3D")
)
