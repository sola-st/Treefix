# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
arr = np.arange(100, dtype=np.intp)

result = libalgos.ensure_platform_int(arr)
assert result is arr
