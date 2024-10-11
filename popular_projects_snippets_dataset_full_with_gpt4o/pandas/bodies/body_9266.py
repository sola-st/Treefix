# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# numpy will auto reshape when all of the tuples are the
# same len, so add an extra one with 2 items and slice it off
values = np.array(
    [
        (Timestamp("2010-01-01"),),
        (Timestamp("2010-01-02"),),
        (Timestamp("2010-01-01"),),
        (Timestamp("2010-01-02"),),
        ("a", "b"),
    ],
    dtype=object,
)[:-1]
result = Categorical(values)
expected = Index(
    [(Timestamp("2010-01-01"),), (Timestamp("2010-01-02"),)],
    tupleize_cols=False,
)
tm.assert_index_equal(result.categories, expected)
