# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_reindex.py
idx = MultiIndex.from_tuples([(0, 0), (1, 1), (1, 1), (2, 2)])
a = pd.Series(np.arange(4), index=idx)
new_idx = MultiIndex.from_tuples([(0, 0), (1, 1), (2, 2)])

msg = "cannot handle a non-unique multi-index!"
with pytest.raises(ValueError, match=msg):
    a.reindex(new_idx)
