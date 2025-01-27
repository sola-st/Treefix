# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_formats.py
levels = [Index(["a/\u03c3", "b/\u03c3", "c/\u03c3"]), Index([0, 1])]
codes = [np.arange(3).repeat(2), np.tile(np.arange(2), 3)]
index = MultiIndex(levels=levels, codes=codes)

repr(index.levels)
repr(index.get_level_values(1))
