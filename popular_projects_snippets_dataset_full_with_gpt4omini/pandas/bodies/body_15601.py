# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH32414
cat = Categorical(input)
ser = Series(cat).fillna(input_fillna)
filled = cat.fillna(ser)
result = cat.fillna(filled)
expected = Categorical(expected_data, categories=expected_categories)
tm.assert_categorical_equal(result, expected)
