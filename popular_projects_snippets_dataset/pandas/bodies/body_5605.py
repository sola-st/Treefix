# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# see GH 17108
result = pd.unique(arg)
tm.assert_numpy_array_equal(result, expected)
