# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_value_counts.py
idx = PeriodIndex(
    [
        "2013-01-01 09:00",
        "2013-01-01 09:00",
        "2013-01-01 09:00",
        "2013-01-01 08:00",
        "2013-01-01 08:00",
        NaT,
    ],
    freq="H",
)
self._check_value_counts_dropna(idx)
