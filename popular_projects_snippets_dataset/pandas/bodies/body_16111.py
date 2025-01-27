# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH 9322
from pandas.core.indexes.accessors import (
    CombinedDatetimelikeProperties,
    DatetimeProperties,
)

assert Series.dt is CombinedDatetimelikeProperties

ser = Series(date_range("2000-01-01", periods=3))
assert isinstance(ser.dt, DatetimeProperties)
