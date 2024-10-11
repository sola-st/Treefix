# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_map.py
# GH 31202 - override base class since we want to maintain categorical/ordered
index = CategoricalIndex(data, categories=categories, ordered=ordered)
result = index.map(str)
expected = CategoricalIndex(
    map(str, data), categories=map(str, categories), ordered=ordered
)
tm.assert_index_equal(result, expected)
