# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_construct_from_scalar.py
# see gh-19565
#
# Categorical result from scalar did not maintain
# categories and ordering of the passed dtype.
cats = ["a", "b", "c"]
cat_type = CategoricalDtype(categories=cats, ordered=False)
expected = Categorical(["a", "a"], categories=cats)

result = construct_1d_arraylike_from_scalar("a", len(expected), cat_type)
tm.assert_categorical_equal(result, expected)
