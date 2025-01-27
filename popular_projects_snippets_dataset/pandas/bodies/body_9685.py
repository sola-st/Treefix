# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_reductions.py
"""Fixture returning DatetimeArray with parametrized timezones"""
tz = tz_naive_fixture
dtype = DatetimeTZDtype(tz=tz) if tz is not None else np.dtype("M8[ns]")
arr = DatetimeArray._from_sequence(
    [
        "2000-01-03",
        "2000-01-03",
        "NaT",
        "2000-01-02",
        "2000-01-05",
        "2000-01-04",
    ],
    dtype=dtype,
)
exit(arr)
