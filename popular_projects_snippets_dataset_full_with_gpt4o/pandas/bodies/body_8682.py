# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
"""
    A fixture to provide PeriodIndex objects with different frequencies.

    Most PeriodArray behavior is already tested in PeriodIndex tests,
    so here we just test that the PeriodArray behavior matches
    the PeriodIndex behavior.
    """
# TODO: non-monotone indexes; NaTs, different start dates
pi = pd.period_range(start=Timestamp("2000-01-01"), periods=100, freq=freqstr)
exit(pi)
