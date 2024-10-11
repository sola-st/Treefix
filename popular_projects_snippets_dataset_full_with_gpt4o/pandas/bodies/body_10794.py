# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH9049: ensure backward compatibility
levels = pd.date_range("2014-01-01", periods=4)
codes = np.random.randint(0, 4, size=100)

cats = Categorical.from_codes(codes, levels, ordered=True)

data = DataFrame(np.random.randn(100, 4))
result = data.groupby(cats, observed=False).mean()

expected = data.groupby(np.asarray(cats), observed=False).mean()
expected = expected.reindex(levels)
expected.index = CategoricalIndex(
    expected.index, categories=expected.index, ordered=True
)

tm.assert_frame_equal(result, expected)

grouped = data.groupby(cats, observed=False)
desc_result = grouped.describe()

idx = cats.codes.argsort()
ord_labels = cats.take(idx)
ord_data = data.take(idx)
expected = ord_data.groupby(ord_labels, observed=False).describe()
tm.assert_frame_equal(desc_result, expected)
tm.assert_index_equal(desc_result.index, expected.index)
tm.assert_index_equal(
    desc_result.index.get_level_values(0), expected.index.get_level_values(0)
)

# GH 10460
expc = Categorical.from_codes(np.arange(4).repeat(8), levels, ordered=True)
exp = CategoricalIndex(expc)
tm.assert_index_equal((desc_result.stack().index.get_level_values(0)), exp)
exp = Index(["count", "mean", "std", "min", "25%", "50%", "75%", "max"] * 4)
tm.assert_index_equal((desc_result.stack().index.get_level_values(1)), exp)
