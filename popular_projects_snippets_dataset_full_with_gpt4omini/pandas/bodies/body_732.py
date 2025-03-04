# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
assert is_integer(1)
assert is_integer(np.int64(1))

assert not is_integer(True)
assert not is_integer(1.1)
assert not is_integer(1 + 3j)
assert not is_integer(False)
assert not is_integer(np.bool_(False))
assert not is_integer(np.float64(1.1))
assert not is_integer(np.complex128(1 + 3j))
assert not is_integer(np.nan)
assert not is_integer(None)
assert not is_integer("x")
assert not is_integer(datetime(2011, 1, 1))
assert not is_integer(np.datetime64("2011-01-01"))
assert not is_integer(Timestamp("2011-01-01"))
assert not is_integer(Timestamp("2011-01-01", tz="US/Eastern"))
assert not is_integer(timedelta(1000))
assert not is_integer(Timedelta("1 days"))
assert not is_integer(np.timedelta64(1, "D"))
