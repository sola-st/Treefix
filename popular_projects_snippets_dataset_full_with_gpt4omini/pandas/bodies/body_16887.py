# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
arr = np.random.randn(1000)

factor = qcut(arr, 10, labels=False)
assert len(np.unique(factor)) == 10
