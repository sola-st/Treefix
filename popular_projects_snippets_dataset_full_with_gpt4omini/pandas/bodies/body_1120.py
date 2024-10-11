# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH 8737
# empty indexer
multi_index = MultiIndex.from_product((["foo", "bar", "baz"], ["alpha", "beta"]))
df = DataFrame(np.random.randn(5, 6), index=range(5), columns=multi_index)
df = df.sort_index(level=0, axis=1)

expected = DataFrame(index=range(5), columns=multi_index.reindex([])[0])
result = df.loc[:, columns_indexer]
tm.assert_frame_equal(result, expected)
