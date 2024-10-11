# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
old = Index([1, 5, 10])
new = Index(list(range(12)))

filler = libalgos.pad["int64_t"](old.values, new.values)

expect_filler = np.array([-1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2], dtype=np.intp)
tm.assert_numpy_array_equal(filler, expect_filler)

# corner case
old = Index([5, 10])
new = Index(np.arange(5, dtype=np.int64))
filler = libalgos.pad["int64_t"](old.values, new.values)
expect_filler = np.array([-1, -1, -1, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(filler, expect_filler)
