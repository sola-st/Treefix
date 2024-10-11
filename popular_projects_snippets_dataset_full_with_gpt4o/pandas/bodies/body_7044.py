# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_constructors.py
# construction with CategoricalDtype
# GH#18109
data, cats, ordered = "a a b b".split(), "c b a".split(), True
dtype = CategoricalDtype(categories=cats, ordered=ordered)

result = CategoricalIndex(data, dtype=dtype)
expected = CategoricalIndex(data, categories=cats, ordered=ordered)
tm.assert_index_equal(result, expected, exact=True)

# GH#19032
result = Index(data, dtype=dtype)
tm.assert_index_equal(result, expected, exact=True)

# error when combining categories/ordered and dtype kwargs
msg = "Cannot specify `categories` or `ordered` together with `dtype`."
with pytest.raises(ValueError, match=msg):
    CategoricalIndex(data, categories=cats, dtype=dtype)

with pytest.raises(ValueError, match=msg):
    CategoricalIndex(data, ordered=ordered, dtype=dtype)
