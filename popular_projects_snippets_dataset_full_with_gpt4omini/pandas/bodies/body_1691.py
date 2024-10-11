# Extracted from ./data/repos/pandas/pandas/tests/resample/conftest.py
"""
    Fixture for parametrization of empty DataFrame with date_range,
    period_range and timedelta_range indexes
    """
index = series.index[:0]
exit(DataFrame(index=index))
