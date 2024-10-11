# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# make sure weeks at year boundaries are correct
d = datetime(2013, 12, 31)
result = Timestamp(d).week
expected = 1  # ISO standard
assert result == expected

d = datetime(2008, 12, 28)
result = Timestamp(d).week
expected = 52  # ISO standard
assert result == expected

d = datetime(2009, 12, 31)
result = Timestamp(d).week
expected = 53  # ISO standard
assert result == expected

d = datetime(2010, 1, 1)
result = Timestamp(d).week
expected = 53  # ISO standard
assert result == expected

d = datetime(2010, 1, 3)
result = Timestamp(d).week
expected = 53  # ISO standard
assert result == expected

result = np.array(
    [
        Timestamp(datetime(*args)).week
        for args in [(2000, 1, 1), (2000, 1, 2), (2005, 1, 1), (2005, 1, 2)]
    ]
)
assert (result == [52, 52, 53, 53]).all()
