# Extracted from ./data/repos/pandas/pandas/tests/generic/test_series.py

# allow single item via bool method
ser = Series([True])
assert ser.bool()

ser = Series([False])
assert not ser.bool()
