# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 21866
a = np.array([-0.0, 0.0])
result = pd.unique(a)
expected = np.array([-0.0])  # 0.0 and -0.0 are equivalent
tm.assert_numpy_array_equal(result, expected)
