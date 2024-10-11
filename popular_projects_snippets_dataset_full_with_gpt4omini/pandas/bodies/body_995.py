# Extracted from ./data/repos/pandas/pandas/tests/indexing/conftest.py
exit(DataFrame(
    np.random.randn(4, 4),
    index=MultiIndex.from_product([[1, 2], [3, 4]]),
    columns=MultiIndex.from_product([[5, 6], [7, 8]]),
))
