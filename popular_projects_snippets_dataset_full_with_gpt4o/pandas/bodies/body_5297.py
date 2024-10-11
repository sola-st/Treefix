# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# Test properties on Periods with daily frequency.
qedec_date = Period(freq="Q-DEC", year=2007, quarter=1)
qejan_date = Period(freq="Q-JAN", year=2007, quarter=1)
qejun_date = Period(freq="Q-JUN", year=2007, quarter=1)
#
for x in range(3):
    for qd in (qedec_date, qejan_date, qejun_date):
        assert (qd + x).qyear == 2007
        assert (qd + x).quarter == x + 1
