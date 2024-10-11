# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
arr = np.random.randint(0, 100, size=50)

result = algos.unique(arr)
assert isinstance(result, np.ndarray)
