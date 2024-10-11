# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
c1 = Categorical([np.nan])
c2 = Categorical([np.nan])
result = union_categoricals([c1, c2], sort_categories=False)
expected = Categorical([np.nan, np.nan])
tm.assert_categorical_equal(result, expected)
