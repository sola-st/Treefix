# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH-36991
cidx = pd.CategoricalIndex(labels, categories=sorted(labels), ordered=ordered)
cidx2 = pd.CategoricalIndex(["u", "v"], ordered=ordered)
midx = MultiIndex.from_product([cidx, cidx2])
df = DataFrame([sorted(data)], columns=midx)
result = df.stack([0, 1])

s_cidx = pd.CategoricalIndex(sorted(labels), ordered=ordered)
expected = Series(data, index=MultiIndex.from_product([[0], s_cidx, cidx2]))

tm.assert_series_equal(result, expected)
