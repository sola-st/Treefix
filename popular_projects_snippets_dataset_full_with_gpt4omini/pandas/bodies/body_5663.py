# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
a = np.random.randint(0, 1000, 100).astype(np.intp)
b = np.random.randint(0, 1000, 100).astype(np.intp)

result = libalgos.groupsort_indexer(a, 1000)[0]

# need to use a stable sort
# np.argsort returns int, groupsort_indexer
# always returns intp
expected = np.argsort(a, kind="mergesort")
expected = expected.astype(np.intp)

tm.assert_numpy_array_equal(result, expected)

# compare with lexsort
# np.lexsort returns int, groupsort_indexer
# always returns intp
key = a * 1000 + b
result = libalgos.groupsort_indexer(key, 1000000)[0]
expected = np.lexsort((b, a))
expected = expected.astype(np.intp)

tm.assert_numpy_array_equal(result, expected)
