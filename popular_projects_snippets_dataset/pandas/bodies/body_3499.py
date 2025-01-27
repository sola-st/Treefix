# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py

obj.iloc[0] = index._na_value
obj.iloc[-1] = index._na_value

# result should be invariant to shuffling
indexer = np.arange(len(index), dtype=np.intp)
np.random.shuffle(indexer)
obj = obj.iloc[indexer]

qs = [0.5, 0, 1]
result = self.compute_quantile(obj, qs)

# expected here assumes len(index) == 9
expected = Series(
    [index[4], index[1], index[-2]], dtype=index.dtype, index=qs, name="A"
)
expected = type(obj)(expected)
tm.assert_equal(result, expected)
