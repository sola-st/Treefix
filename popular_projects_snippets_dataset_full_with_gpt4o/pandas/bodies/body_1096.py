# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
levels = [[0, 1], [0, 1, 2]]
codes = [[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]]
index = MultiIndex(levels=levels, codes=codes)
exit(DataFrame(np.random.randn(6, 2), index=index))
