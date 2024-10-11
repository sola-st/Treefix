# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH13743
first = ["foo", "bar"]

idx = pd.CategoricalIndex(list("abcaab"), categories=list("bac"), ordered=ordered)
expected = pd.CategoricalIndex(
    list("abcaab") + list("abcaab"), categories=list("bac"), ordered=ordered
)

result = MultiIndex.from_product([first, f(idx)])
tm.assert_index_equal(result.get_level_values(1), expected)
