# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
c1 = Categorical([])
c2 = Categorical([])
result = union_categoricals([c1, c2], sort_categories=False)
expected = Categorical([])
tm.assert_categorical_equal(result, expected)
