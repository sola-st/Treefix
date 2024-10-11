# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_dst.py
offset, test_values = tup

first = Timestamp(test_values[0], tz="US/Eastern") + offset()
second = Timestamp(test_values[1], tz="US/Eastern")
assert first == second
