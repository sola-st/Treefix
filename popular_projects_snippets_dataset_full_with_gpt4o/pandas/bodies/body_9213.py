# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_replace.py
# GH#26988
cat = Categorical(["a", "b"])
expected = Categorical(result)
result = pd.Series(cat).replace(to_replace, value)._values

tm.assert_categorical_equal(result, expected)
if to_replace == "b":  # the "c" test is supposed to be unchanged
    with pytest.raises(AssertionError, match=expected_error_msg):
        # ensure non-inplace call does not affect original
        tm.assert_categorical_equal(cat, expected)

pd.Series(cat).replace(to_replace, value, inplace=True)
tm.assert_categorical_equal(cat, expected)
