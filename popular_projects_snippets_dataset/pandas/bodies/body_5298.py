# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# Test properties on Periods with daily frequency.
m_date = Period(freq="M", year=2007, month=1)
for x in range(11):
    m_ival_x = m_date + x
    assert m_ival_x.year == 2007
    if 1 <= x + 1 <= 3:
        assert m_ival_x.quarter == 1
    elif 4 <= x + 1 <= 6:
        assert m_ival_x.quarter == 2
    elif 7 <= x + 1 <= 9:
        assert m_ival_x.quarter == 3
    elif 10 <= x + 1 <= 12:
        assert m_ival_x.quarter == 4
    assert m_ival_x.month == x + 1
