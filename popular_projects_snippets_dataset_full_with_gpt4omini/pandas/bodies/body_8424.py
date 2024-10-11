# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
rng1 = list(generate_range(START, END, periods=None, offset=CDay(), unit="ns"))
rng2 = list(generate_range(START, END, periods=None, offset="C", unit="ns"))
assert rng1 == rng2
