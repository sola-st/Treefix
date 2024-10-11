# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# can select values that are IN the range of a value
i = IntervalIndex.from_arrays([0, 1], [1, 2])

expected = np.array([False, False], dtype="bool")
actual = i.contains(0)
tm.assert_numpy_array_equal(actual, expected)
actual = i.contains(3)
tm.assert_numpy_array_equal(actual, expected)

expected = np.array([True, False], dtype="bool")
actual = i.contains(0.5)
tm.assert_numpy_array_equal(actual, expected)
actual = i.contains(1)
tm.assert_numpy_array_equal(actual, expected)

# __contains__ not implemented for "interval in interval", follow
# that for the contains method for now
with pytest.raises(
    NotImplementedError, match="contains not implemented for two"
):
    i.contains(Interval(0, 1))
