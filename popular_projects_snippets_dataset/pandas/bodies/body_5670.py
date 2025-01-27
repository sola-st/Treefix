# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp = Series([1], dtype=int)
tm.assert_numpy_array_equal(algos.mode([1]), exp.values)

exp = Series(["a", "b", "c"], dtype=object)
tm.assert_numpy_array_equal(algos.mode(["a", "b", "c"]), exp.values)
