# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py
# GH#25464
ci = tm.makeCategoricalIndex(100)
msg = "When changing to a larger dtype, its size must be a divisor"
with pytest.raises(ValueError, match=msg):
    ci.view("i8")
with pytest.raises(ValueError, match=msg):
    ci._data.view("i8")

ci = ci[:-4]  # length divisible by 8

res = ci.view("i8")
expected = ci._data.codes.view("i8")
tm.assert_numpy_array_equal(res, expected)

cat = ci._data
tm.assert_numpy_array_equal(cat.view("i8"), expected)
