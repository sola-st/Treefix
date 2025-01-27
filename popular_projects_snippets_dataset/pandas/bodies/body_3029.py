# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_timestamp.py
exit(date_range(
    to_datetime("1/1/2001") + delta,
    to_datetime("12/31/2009") + delta,
    freq=freq,
))
