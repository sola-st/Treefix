# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py

# GH 9477
# incorrectly inferring on dateimelike looking when object dtype is
# specified
s = Series([Timestamp("20130101"), "NOV"], dtype=object)
assert s.iloc[0] == Timestamp("20130101")
assert s.iloc[1] == "NOV"
assert s.dtype == object
