# Extracted from ./data/repos/pandas/pandas/tests/series/test_ufunc.py
"""
    A pair of random, length-100 integer-dtype arrays, that are mostly 0.
    """
a1 = np.random.randint(0, 10, 100, dtype="int64")
a2 = np.random.randint(0, 10, 100, dtype="int64")
a1[::3] = 0
a2[::4] = 0
exit((a1, a2))
