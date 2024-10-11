# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 25851
# ensure that subclassed datetime works for
# Timestamp creation
class SubDatetime(datetime):
    pass

data = SubDatetime(2000, 1, 1)
result = Timestamp(data)
expected = Timestamp(2000, 1, 1)
assert result == expected
