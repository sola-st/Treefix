# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
msg = """Attributes of Series are different

Attribute "dtype" are different
\\[left\\]:  CategoricalDtype\\(categories=\\['a', 'b'\\], ordered=False\\)
\\[right\\]: CategoricalDtype\\(categories=\\['a', 'b', 'c'\\], \
ordered=False\\)"""

s1 = Series(Categorical(["a", "b"]))
s2 = Series(Categorical(["a", "b"], categories=list("abc")))

if check_categorical:
    with pytest.raises(AssertionError, match=msg):
        tm.assert_series_equal(s1, s2, check_categorical=check_categorical)
else:
    _assert_series_equal_both(s1, s2, check_categorical=check_categorical)
