# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
rng = timedelta_range("1 days", periods=10.5)
exp = timedelta_range("1 days", periods=10)
tm.assert_index_equal(rng, exp)

msg = "periods must be a number, got foo"
with pytest.raises(TypeError, match=msg):
    timedelta_range(start="1 days", periods="foo", freq="D")

msg = (
    r"TimedeltaIndex\(\.\.\.\) must be called with a collection of some kind, "
    "'1 days' was passed"
)
with pytest.raises(TypeError, match=msg):
    TimedeltaIndex("1 days")

# generator expression
gen = (timedelta(i) for i in range(10))
result = TimedeltaIndex(gen)
expected = TimedeltaIndex([timedelta(i) for i in range(10)])
tm.assert_index_equal(result, expected)

# NumPy string array
strings = np.array(["1 days", "2 days", "3 days"])
result = TimedeltaIndex(strings)
expected = to_timedelta([1, 2, 3], unit="d")
tm.assert_index_equal(result, expected)

from_ints = TimedeltaIndex(expected.asi8)
tm.assert_index_equal(from_ints, expected)

# non-conforming freq
msg = (
    "Inferred frequency None from passed values does not conform to "
    "passed frequency D"
)
with pytest.raises(ValueError, match=msg):
    TimedeltaIndex(["1 days", "2 days", "4 days"], freq="D")

msg = (
    "Of the four parameters: start, end, periods, and freq, exactly "
    "three must be specified"
)
with pytest.raises(ValueError, match=msg):
    timedelta_range(periods=10, freq="D")
