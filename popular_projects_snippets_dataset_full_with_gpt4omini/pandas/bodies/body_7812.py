# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_value_counts.py
idx = TimedeltaIndex(
    [
        "1 days 09:00:00",
        "1 days 09:00:00",
        "1 days 09:00:00",
        "1 days 08:00:00",
        "1 days 08:00:00",
        NaT,
    ]
)
self._check_value_counts_dropna(idx)
