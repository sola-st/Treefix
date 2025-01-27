# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_astype.py
# GH#10696/GH#18593
data = list("abcaacbab")
cat = Categorical(data, categories=list("bac"), ordered=cat_ordered)

# standard categories
dtype = CategoricalDtype(ordered=dtype_ordered)
result = cat.astype(dtype)
expected = Categorical(data, categories=cat.categories, ordered=dtype_ordered)
tm.assert_categorical_equal(result, expected)

# non-standard categories
dtype = CategoricalDtype(list("adc"), dtype_ordered)
result = cat.astype(dtype)
expected = Categorical(data, dtype=dtype)
tm.assert_categorical_equal(result, expected)

if dtype_ordered is False:
    # dtype='category' can't specify ordered, so only test once
    result = cat.astype("category")
    expected = cat
    tm.assert_categorical_equal(result, expected)
