# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# validate all units, GH 6855, GH 21762
# array-likes
expected = TimedeltaIndex(
    [np.timedelta64(i, np_unit) for i in np.arange(5).tolist()],
    dtype="m8[ns]",
)
# TODO(2.0): the desired output dtype may have non-nano resolution
result = to_timedelta(wrapper(range(5)), unit=unit)
tm.assert_index_equal(result, expected)
result = TimedeltaIndex(wrapper(range(5)), unit=unit)
tm.assert_index_equal(result, expected)

str_repr = [f"{x}{unit}" for x in np.arange(5)]
result = to_timedelta(wrapper(str_repr))
tm.assert_index_equal(result, expected)
result = to_timedelta(wrapper(str_repr))
tm.assert_index_equal(result, expected)

# scalar
expected = Timedelta(np.timedelta64(2, np_unit).astype("timedelta64[ns]"))
result = to_timedelta(2, unit=unit)
assert result == expected
result = Timedelta(2, unit=unit)
assert result == expected

result = to_timedelta(f"2{unit}")
assert result == expected
result = Timedelta(f"2{unit}")
assert result == expected
