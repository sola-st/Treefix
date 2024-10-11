# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
# GH 13759
res = union_categoricals(
    [Categorical([1, 2, np.nan]), Categorical([3, 2, np.nan])]
)
exp = Categorical([1, 2, np.nan, 3, 2, np.nan])
tm.assert_categorical_equal(res, exp)

res = union_categoricals(
    [Categorical(["A", "B"]), Categorical(["B", "B", np.nan])]
)
exp = Categorical(["A", "B", "B", "B", np.nan])
tm.assert_categorical_equal(res, exp)

val1 = [pd.Timestamp("2011-01-01"), pd.Timestamp("2011-03-01"), pd.NaT]
val2 = [pd.NaT, pd.Timestamp("2011-01-01"), pd.Timestamp("2011-02-01")]

res = union_categoricals([Categorical(val1), Categorical(val2)])
exp = Categorical(
    val1 + val2,
    categories=[
        pd.Timestamp("2011-01-01"),
        pd.Timestamp("2011-03-01"),
        pd.Timestamp("2011-02-01"),
    ],
)
tm.assert_categorical_equal(res, exp)

# all NaN
res = union_categoricals(
    [
        Categorical(np.array([np.nan, np.nan], dtype=object)),
        Categorical(["X"]),
    ]
)
exp = Categorical([np.nan, np.nan, "X"])
tm.assert_categorical_equal(res, exp)

res = union_categoricals(
    [Categorical([np.nan, np.nan]), Categorical([np.nan, np.nan])]
)
exp = Categorical([np.nan, np.nan, np.nan, np.nan])
tm.assert_categorical_equal(res, exp)
