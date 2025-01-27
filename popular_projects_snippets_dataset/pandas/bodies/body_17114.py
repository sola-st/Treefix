# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
c1 = Categorical(["x", np.nan])
c2 = Categorical([np.nan, "b"])
result = union_categoricals([c1, c2], sort_categories=False)
expected = Categorical(["x", np.nan, np.nan, "b"], categories=["x", "b"])
tm.assert_categorical_equal(result, expected)
