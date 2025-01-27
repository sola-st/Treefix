# Extracted from ./data/repos/pandas/pandas/tests/indexing/conftest.py
exit(DataFrame(
    np.random.randn(4, 4), index=np.arange(0, 8, 2), columns=np.arange(0, 12, 3)
))
