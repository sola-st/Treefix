# Extracted from ./data/repos/pandas/pandas/tests/indexes/object/test_indexing.py
expected_missing = np.array([], dtype=np.intp)
# matching-but-not-identical nats
if is_matching_na(np_nat_fixture, np_nat_fixture2):
    # ensure nats are different objects
    index = Index(
        np.array(
            ["2021-10-02", np_nat_fixture.copy(), np_nat_fixture2.copy()],
            dtype=object,
        ),
        dtype=object,
    )
    # pass as index to prevent target from being casted to DatetimeIndex
    indexer, missing = index.get_indexer_non_unique(
        Index([np_nat_fixture], dtype=object)
    )
    expected_indexer = np.array([1, 2], dtype=np.intp)
    tm.assert_numpy_array_equal(indexer, expected_indexer)
    tm.assert_numpy_array_equal(missing, expected_missing)
# dt64nat vs td64nat
else:
    try:
        np_nat_fixture == np_nat_fixture2
    except (TypeError, OverflowError):
        # Numpy will raise on uncomparable types, like
        # np.datetime64('NaT', 'Y') and np.datetime64('NaT', 'ps')
        # https://github.com/numpy/numpy/issues/22762
        exit()
    index = Index(
        np.array(
            [
                "2021-10-02",
                np_nat_fixture,
                np_nat_fixture2,
                np_nat_fixture,
                np_nat_fixture2,
            ],
            dtype=object,
        ),
        dtype=object,
    )
    # pass as index to prevent target from being casted to DatetimeIndex
    indexer, missing = index.get_indexer_non_unique(
        Index([np_nat_fixture], dtype=object)
    )
    expected_indexer = np.array([1, 3], dtype=np.intp)
    tm.assert_numpy_array_equal(indexer, expected_indexer)
    tm.assert_numpy_array_equal(missing, expected_missing)
