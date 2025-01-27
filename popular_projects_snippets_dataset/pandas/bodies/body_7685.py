# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
dt_index = date_range("2000-01-01", periods=2)
mi = MultiIndex.from_product([[1, 2], dt_index])
etalon = construct_1d_object_array_from_listlike(
    [
        (1, Timestamp("2000-01-01")),
        (1, Timestamp("2000-01-02")),
        (2, Timestamp("2000-01-01")),
        (2, Timestamp("2000-01-02")),
    ]
)
tm.assert_numpy_array_equal(mi.values, etalon)
