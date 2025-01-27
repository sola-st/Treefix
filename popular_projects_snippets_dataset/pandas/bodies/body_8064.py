# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 12756
if isinstance(index, CategoricalIndex):
    # Tested in test_categorical
    exit()
elif not index.is_unique:
    # Cannot map duplicated index
    exit()

rng = np.arange(len(index), 0, -1, dtype=np.int64)

if index.empty:
    # to match proper result coercion for uints
    expected = Index([])
elif is_numeric_dtype(index.dtype):
    expected = index._constructor(rng, dtype=index.dtype)
elif type(index) is Index and index.dtype != object:
    # i.e. EA-backed, for now just Nullable
    expected = Index(rng, dtype=index.dtype)
else:
    expected = Index(rng)

result = index.map(mapper(expected, index))
tm.assert_index_equal(result, expected)
