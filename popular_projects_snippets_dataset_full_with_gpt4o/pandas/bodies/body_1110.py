# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
single_level = single_level_multiindex
s = Series(np.random.randn(len(single_level)), index=single_level)
for k in single_level.values:
    s[k]
