# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
arr = np.random.randn(100)
arr[:20] = np.nan

result = qcut(arr, 4)
assert isna(result[:20]).all()
