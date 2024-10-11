# Extracted from ./data/repos/pandas/pandas/tests/indexes/object/test_indexing.py
# GH#22332
# check pairwise, that no pair of na values
# is mangled
if unique_nulls_fixture is unique_nulls_fixture2:
    exit()  # skip it, values are not unique
arr = np.array([unique_nulls_fixture, unique_nulls_fixture2], dtype=object)
index = Index(arr, dtype=object)
result = index.get_indexer(
    [unique_nulls_fixture, unique_nulls_fixture2, "Unknown"]
)
expected = np.array([0, 1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
