# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
# GH18203
result = repr(Grouper(key="A", freq="H"))
expected = (
    "TimeGrouper(key='A', freq=<Hour>, axis=0, sort=True, dropna=True, "
    "closed='left', label='left', how='mean', "
    "convention='e', origin='start_day')"
)
assert result == expected

result = repr(Grouper(key="A", freq="H", origin="2000-01-01"))
expected = (
    "TimeGrouper(key='A', freq=<Hour>, axis=0, sort=True, dropna=True, "
    "closed='left', label='left', how='mean', "
    "convention='e', origin=Timestamp('2000-01-01 00:00:00'))"
)
assert result == expected
