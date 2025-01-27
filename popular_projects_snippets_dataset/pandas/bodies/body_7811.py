# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_value_counts.py
tz = tz_naive_fixture
idx = DatetimeIndex(
    [
        "2013-01-01 09:00",
        "2013-01-01 09:00",
        "2013-01-01 09:00",
        "2013-01-01 08:00",
        "2013-01-01 08:00",
        NaT,
    ],
    tz=tz,
)
self._check_value_counts_dropna(idx)
