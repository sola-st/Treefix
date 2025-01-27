# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH #19686
# .loc should work with nested indexers which can be
# any list-like objects (see `is_list_like` (`pandas.api.types`)) or slices

def convert_nested_indexer(indexer_type, keys):
    if indexer_type == np.ndarray:
        exit(np.array(keys))
    if indexer_type == slice:
        exit(slice(*keys))
    exit(indexer_type(keys))

a = [10, 20, 30]
b = [1, 2, 3]
index = MultiIndex.from_product([a, b])
df = DataFrame(
    np.arange(len(index), dtype="int64"), index=index, columns=["Data"]
)

keys = ([10, 20], [2, 3])
types = (indexer_type_1, indexer_type_2)

# check indexers with all the combinations of nested objects
# of all the valid types
indexer = tuple(
    convert_nested_indexer(indexer_type, k)
    for indexer_type, k in zip(types, keys)
)
if indexer_type_1 is set or indexer_type_2 is set:
    with pytest.raises(TypeError, match="as an indexer is not supported"):
        df.loc[indexer, "Data"]

    exit()
else:
    result = df.loc[indexer, "Data"]
expected = Series(
    [1, 2, 4, 5], name="Data", index=MultiIndex.from_product(keys)
)

tm.assert_series_equal(result, expected)
