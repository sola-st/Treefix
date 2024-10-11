# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
obj.iloc[:] = index._na_value
# Check dtypes were preserved; this was once a problem see GH#39763
assert np.all(obj.dtypes == index.dtype)

# result should be invariant to shuffling
indexer = np.arange(len(index), dtype=np.intp)
np.random.shuffle(indexer)
obj = obj.iloc[indexer]

qs = [0.5, 0, 1]
result = self.compute_quantile(obj, qs)

expected = index.take([-1, -1, -1], allow_fill=True, fill_value=index._na_value)
expected = Series(expected, index=qs, name="A")
expected = type(obj)(expected)
tm.assert_equal(result, expected)
