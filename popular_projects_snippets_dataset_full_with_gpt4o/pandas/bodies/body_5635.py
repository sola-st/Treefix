# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
np.random.seed(1234)
from pandas.core.reshape.tile import cut

arr = np.random.randn(4)
factor = cut(arr, 4)

# assert isinstance(factor, n)
result = algos.value_counts(factor)
breaks = [-1.194, -0.535, 0.121, 0.777, 1.433]
index = IntervalIndex.from_breaks(breaks).astype(CDT(ordered=True))
expected = Series([1, 1, 1, 1], index=index)
tm.assert_series_equal(result.sort_index(), expected.sort_index())
