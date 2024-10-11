# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
d = {datetime(2011, 1, 1): 5}
stamp = Timestamp(datetime(2011, 1, 1))
assert d[stamp] == 5
