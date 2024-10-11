# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 17927
result = pd.unique(array)
tm.assert_numpy_array_equal(result, expected)
