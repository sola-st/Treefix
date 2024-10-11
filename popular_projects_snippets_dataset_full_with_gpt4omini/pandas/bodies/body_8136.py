# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH34123
# TODO: also this op right now produces FutureWarning from numpy
#  https://github.com/numpy/numpy/issues/11521
idx = Index([("a", "b"), ("b", "c"), ("c", "a")])
result = idx == ("c", "a")
expected = np.array([False, False, True])
tm.assert_numpy_array_equal(result, expected)
