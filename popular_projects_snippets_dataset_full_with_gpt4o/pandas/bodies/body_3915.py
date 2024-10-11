# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH13854
cidx = pd.CategoricalIndex(labels, categories=list("xyz"), ordered=ordered)
df = DataFrame([[10, 11, 12]], columns=cidx)
result = df.stack()

# `MultiIndex.from_product` preserves categorical dtype -
# it's tested elsewhere.
midx = MultiIndex.from_product([df.index, cidx])
expected = Series([10, 11, 12], index=midx)

tm.assert_series_equal(result, expected)
