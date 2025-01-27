# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
c = cut(range(5), 3)
expected = c
result = cut(range(5), bins=expected.categories)
tm.assert_categorical_equal(result, expected)

expected = Categorical.from_codes(
    np.append(c.codes, -1), categories=c.categories, ordered=True
)
result = cut(range(6), bins=expected.categories)
tm.assert_categorical_equal(result, expected)
