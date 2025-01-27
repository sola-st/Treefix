# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19738
td = Timedelta(10, unit="d")

result = op(td, datetime(2016, 1, 1))
if op is operator.add:
    # datetime + Timedelta does _not_ call Timedelta.__radd__,
    # so we get a datetime back instead of a Timestamp
    assert isinstance(result, Timestamp)
assert result == Timestamp(2016, 1, 11)

result = op(td, Timestamp("2018-01-12 18:09"))
assert isinstance(result, Timestamp)
assert result == Timestamp("2018-01-22 18:09")

result = op(td, np.datetime64("2018-01-12"))
assert isinstance(result, Timestamp)
assert result == Timestamp("2018-01-22")

result = op(td, NaT)
assert result is NaT
