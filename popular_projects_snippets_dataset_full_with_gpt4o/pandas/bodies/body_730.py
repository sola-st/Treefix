# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py

assert is_number(True)
assert is_number(1)
assert is_number(1.1)
assert is_number(1 + 3j)
assert is_number(np.int64(1))
assert is_number(np.float64(1.1))
assert is_number(np.complex128(1 + 3j))
assert is_number(np.nan)

assert not is_number(None)
assert not is_number("x")
assert not is_number(datetime(2011, 1, 1))
assert not is_number(np.datetime64("2011-01-01"))
assert not is_number(Timestamp("2011-01-01"))
assert not is_number(Timestamp("2011-01-01", tz="US/Eastern"))
assert not is_number(timedelta(1000))
assert not is_number(Timedelta("1 days"))

# questionable
assert not is_number(np.bool_(False))
assert is_number(np.timedelta64(1, "D"))
