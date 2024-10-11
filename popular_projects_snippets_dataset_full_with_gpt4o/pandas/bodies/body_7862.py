# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_shift.py
pi1 = period_range(freq="A", start="1/1/2001", end="12/1/2009")
pi2 = period_range(freq="A", start="1/1/2002", end="12/1/2010")

tm.assert_index_equal(pi1.shift(0), pi1)

assert len(pi1) == len(pi2)
tm.assert_index_equal(pi1.shift(1), pi2)

pi1 = period_range(freq="A", start="1/1/2001", end="12/1/2009")
pi2 = period_range(freq="A", start="1/1/2000", end="12/1/2008")
assert len(pi1) == len(pi2)
tm.assert_index_equal(pi1.shift(-1), pi2)

pi1 = period_range(freq="M", start="1/1/2001", end="12/1/2009")
pi2 = period_range(freq="M", start="2/1/2001", end="1/1/2010")
assert len(pi1) == len(pi2)
tm.assert_index_equal(pi1.shift(1), pi2)

pi1 = period_range(freq="M", start="1/1/2001", end="12/1/2009")
pi2 = period_range(freq="M", start="12/1/2000", end="11/1/2009")
assert len(pi1) == len(pi2)
tm.assert_index_equal(pi1.shift(-1), pi2)

pi1 = period_range(freq="D", start="1/1/2001", end="12/1/2009")
pi2 = period_range(freq="D", start="1/2/2001", end="12/2/2009")
assert len(pi1) == len(pi2)
tm.assert_index_equal(pi1.shift(1), pi2)

pi1 = period_range(freq="D", start="1/1/2001", end="12/1/2009")
pi2 = period_range(freq="D", start="12/31/2000", end="11/30/2009")
assert len(pi1) == len(pi2)
tm.assert_index_equal(pi1.shift(-1), pi2)
