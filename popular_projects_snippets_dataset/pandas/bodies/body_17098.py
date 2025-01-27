# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
# GH 13361
result = union_categoricals([box(Categorical(a)), box(Categorical(b))])
expected = Categorical(combined)
tm.assert_categorical_equal(result, expected)
