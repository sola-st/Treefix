# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py
msg = """Index are different

Attribute "dtype" are different
\\[left\\]:  CategoricalDtype\\(categories=\\['a', 'b'\\], ordered=False\\)
\\[right\\]: CategoricalDtype\\(categories=\\['a', 'b', 'c'\\], \
ordered=False\\)"""

idx1 = Index(Categorical(["a", "b"]))
idx2 = Index(Categorical(["a", "b"], categories=["a", "b", "c"]))

if check_categorical:
    with pytest.raises(AssertionError, match=msg):
        tm.assert_index_equal(idx1, idx2, check_categorical=check_categorical)
else:
    tm.assert_index_equal(idx1, idx2, check_categorical=check_categorical)
