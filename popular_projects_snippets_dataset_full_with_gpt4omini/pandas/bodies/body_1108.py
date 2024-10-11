# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py

# GH6788
# multi-index indexer is None (meaning take all)
attributes = ["Attribute" + str(i) for i in range(1)]
attribute_values = ["Value" + str(i) for i in range(5)]

index = MultiIndex.from_product([attributes, attribute_values])
df = 0.1 * np.random.randn(10, 1 * 5) + 0.5
df = DataFrame(df, columns=index)
result = df[attributes]
tm.assert_frame_equal(result, df)

# GH 7349
# loc with a multi-index seems to be doing fallback
df = DataFrame(
    np.arange(12).reshape(-1, 1),
    index=MultiIndex.from_product([[1, 2, 3, 4], [1, 2, 3]]),
)

expected = df.loc[([1, 2],), :]
result = df.loc[[1, 2]]
tm.assert_frame_equal(result, expected)
