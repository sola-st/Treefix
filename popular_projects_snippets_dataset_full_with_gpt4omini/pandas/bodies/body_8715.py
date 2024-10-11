# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
"""
        Fixture returning DatetimeArray with parametrized frequency and
        timezones
        """
tz = tz_naive_fixture
dti = pd.date_range("2016-01-01 01:01:00", periods=5, freq=freqstr, tz=tz)
dta = dti._data
exit(dta)
