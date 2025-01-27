# Extracted from ./data/repos/pandas/pandas/tests/indexes/object/test_indexing.py
# even though this isn't non-unique, this should still work
index = Index(["a", "b", nulls_fixture])
indexer, missing = index.get_indexer_non_unique([nulls_fixture])

expected_indexer = np.array([2], dtype=np.intp)
expected_missing = np.array([], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected_indexer)
tm.assert_numpy_array_equal(missing, expected_missing)

# actually non-unique
index = Index(["a", nulls_fixture, "b", nulls_fixture])
indexer, missing = index.get_indexer_non_unique([nulls_fixture])

expected_indexer = np.array([1, 3], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected_indexer)
tm.assert_numpy_array_equal(missing, expected_missing)

# matching-but-not-identical nans
if is_matching_na(nulls_fixture, float("NaN")):
    index = Index(["a", float("NaN"), "b", float("NaN")])
    match_but_not_identical = True
elif is_matching_na(nulls_fixture, Decimal("NaN")):
    index = Index(["a", Decimal("NaN"), "b", Decimal("NaN")])
    match_but_not_identical = True
else:
    match_but_not_identical = False

if match_but_not_identical:
    indexer, missing = index.get_indexer_non_unique([nulls_fixture])

    expected_indexer = np.array([1, 3], dtype=np.intp)
    tm.assert_numpy_array_equal(indexer, expected_indexer)
    tm.assert_numpy_array_equal(missing, expected_missing)
