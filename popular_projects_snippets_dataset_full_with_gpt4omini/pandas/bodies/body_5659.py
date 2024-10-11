# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py

old = np.array([], dtype="O")
new = np.array([datetime(2010, 12, 31)], dtype="O")

result = libalgos.pad["object"](old, new)
expected = np.array([-1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)

result = libalgos.pad["object"](new, old)
expected = np.array([], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)

result = libalgos.backfill["object"](old, new)
expected = np.array([-1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)

result = libalgos.backfill["object"](new, old)
expected = np.array([], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
