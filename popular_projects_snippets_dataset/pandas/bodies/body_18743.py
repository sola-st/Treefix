# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture for Series of floats with DatetimeIndex
    """
s = tm.makeTimeSeries()
s.name = "ts"
exit(s)
