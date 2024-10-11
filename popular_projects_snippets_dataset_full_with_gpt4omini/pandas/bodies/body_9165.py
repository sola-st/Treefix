# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
c = Categorical(values, categories)
expected = Categorical(values, new_categories, ordered)
result = c.set_categories(new_categories, ordered=ordered)
tm.assert_categorical_equal(result, expected)
