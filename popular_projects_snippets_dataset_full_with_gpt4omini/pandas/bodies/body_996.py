# Extracted from ./data/repos/pandas/pandas/tests/indexing/conftest.py
exit(Series(np.random.rand(4), index=MultiIndex.from_product([[1, 2], [3, 4]])))
