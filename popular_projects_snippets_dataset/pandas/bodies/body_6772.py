# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
actual = Interval(0, 1) < self.index
expected = np.array([False, True])
tm.assert_numpy_array_equal(actual, expected)

actual = Interval(0.5, 1.5) < self.index
expected = np.array([False, True])
tm.assert_numpy_array_equal(actual, expected)
actual = self.index > Interval(0.5, 1.5)
tm.assert_numpy_array_equal(actual, expected)

actual = self.index == self.index
expected = np.array([True, True])
tm.assert_numpy_array_equal(actual, expected)
actual = self.index <= self.index
tm.assert_numpy_array_equal(actual, expected)
actual = self.index >= self.index
tm.assert_numpy_array_equal(actual, expected)

actual = self.index < self.index
expected = np.array([False, False])
tm.assert_numpy_array_equal(actual, expected)
actual = self.index > self.index
tm.assert_numpy_array_equal(actual, expected)

actual = self.index == IntervalIndex.from_breaks([0, 1, 2], "left")
tm.assert_numpy_array_equal(actual, expected)

actual = self.index == self.index.values
tm.assert_numpy_array_equal(actual, np.array([True, True]))
actual = self.index.values == self.index
tm.assert_numpy_array_equal(actual, np.array([True, True]))
actual = self.index <= self.index.values
tm.assert_numpy_array_equal(actual, np.array([True, True]))
actual = self.index != self.index.values
tm.assert_numpy_array_equal(actual, np.array([False, False]))
actual = self.index > self.index.values
tm.assert_numpy_array_equal(actual, np.array([False, False]))
actual = self.index.values > self.index
tm.assert_numpy_array_equal(actual, np.array([False, False]))

# invalid comparisons
actual = self.index == 0
tm.assert_numpy_array_equal(actual, np.array([False, False]))
actual = self.index == self.index.left
tm.assert_numpy_array_equal(actual, np.array([False, False]))

msg = "|".join(
    [
        "not supported between instances of 'int' and '.*.Interval'",
        r"Invalid comparison between dtype=interval\[int64, right\] and ",
    ]
)
with pytest.raises(TypeError, match=msg):
    self.index > 0
with pytest.raises(TypeError, match=msg):
    self.index <= 0
with pytest.raises(TypeError, match=msg):
    self.index > np.arange(2)

msg = "Lengths must match to compare"
with pytest.raises(ValueError, match=msg):
    self.index > np.arange(3)
