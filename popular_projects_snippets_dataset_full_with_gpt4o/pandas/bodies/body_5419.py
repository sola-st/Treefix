# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
assert get_timezone(Timestamp("2014-11-02 01:00Z").tzinfo) is timezone.utc
