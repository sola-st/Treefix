# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_map.py
orig_values = ["a", "B", 1, "a"]
new_values = ["one", 2, 3.0, "one"]
cur_index = CategoricalIndex(orig_values, name="XXX")
expected = CategoricalIndex(new_values, name="XXX", categories=[3.0, 2, "one"])

mapper = Series(new_values[:-1], index=orig_values[:-1])
result = cur_index.map(mapper)
# Order of categories in result can be different
tm.assert_index_equal(result, expected)

mapper = dict(zip(orig_values[:-1], new_values[:-1]))
result = cur_index.map(mapper)
# Order of categories in result can be different
tm.assert_index_equal(result, expected)
