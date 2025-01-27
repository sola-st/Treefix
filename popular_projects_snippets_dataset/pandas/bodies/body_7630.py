# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#18519 : when combinations of codes cannot be represented in 64
# bits, the index underlying the MultiIndex engine works with Python
# integers, rather than uint64.
N = 5
keys = [
    tuple(arr)
    for arr in [
        [0] * 10 * N,
        [1] * 10 * N,
        [2] * 10 * N,
        [np.nan] * N + [2] * 9 * N,
        [0] * N + [2] * 9 * N,
        [np.nan] * N + [2] * 8 * N + [0] * N,
    ]
]
# Each level contains 4 elements (including NaN), so it is represented
# in 2 bits, for a total of 2*N*10 = 100 > 64 bits. If we were using a
# 64 bit engine and truncating the first levels, the fourth and fifth
# keys would collide; if truncating the last levels, the fifth and
# sixth; if rotating bits rather than shifting, the third and fifth.

for idx, key_value in enumerate(keys):
    index = MultiIndex.from_tuples(keys)
    assert index.get_loc(key_value) == idx

    expected = np.arange(idx + 1, dtype=np.intp)
    result = index.get_indexer([keys[i] for i in expected])
    tm.assert_numpy_array_equal(result, expected)

# With missing key:
idces = range(len(keys))
expected = np.array([-1] + list(idces), dtype=np.intp)
missing = tuple([0, 1] * 5 * N)
result = index.get_indexer([missing] + [keys[i] for i in idces])
tm.assert_numpy_array_equal(result, expected)
