# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
arr = np.random.randn(100)
factor = qcut(arr, [0, 0.25, 0.5, 0.75, 1.0])

expected = qcut(arr, 4)
tm.assert_categorical_equal(factor, expected)
