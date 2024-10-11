# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
# Check that our hash doesn't change because of a mistake
# in the actual code; this is the ground truth.
result = hash_pandas_object(Index(["foo", "bar", "baz"]))
expected = Series(
    np.array(
        [3600424527151052760, 1374399572096150070, 477881037637427054],
        dtype="uint64",
    ),
    index=["foo", "bar", "baz"],
)
tm.assert_series_equal(result, expected)
