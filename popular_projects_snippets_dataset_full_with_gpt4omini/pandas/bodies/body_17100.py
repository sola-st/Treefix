# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
s = Categorical([0, 1.2, 2], ordered=True)
s2 = Categorical([0, 1.2, 2], ordered=True)
result = union_categoricals([s, s2])
expected = Categorical([0, 1.2, 2, 0, 1.2, 2], ordered=True)
tm.assert_categorical_equal(result, expected)
