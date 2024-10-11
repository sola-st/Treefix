# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
data = np.arange(100, dtype="i8") * 24 * 3600 * 10**9
np.random.shuffle(data)

freq = None if self.array_cls is not PeriodArray else "D"

arr = self.array_cls(data, freq=freq)
idx = self.index_cls._simple_new(arr)

takers = [1, 4, 94]
result = arr.take(takers)
expected = idx.take(takers)

tm.assert_index_equal(self.index_cls(result), expected)

takers = np.array([1, 4, 94])
result = arr.take(takers)
expected = idx.take(takers)

tm.assert_index_equal(self.index_cls(result), expected)
