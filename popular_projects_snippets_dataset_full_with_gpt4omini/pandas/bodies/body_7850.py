# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_repeat.py
# GH#10183
expected = PeriodIndex([per for per in index for _ in range(3)])
result = np.repeat(index, 3) if use_numpy else index.repeat(3)
tm.assert_index_equal(result, expected)
assert result.freqstr == index.freqstr
