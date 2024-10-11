# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_append.py
# appending with different categories or reordered is not ok
msg = "all inputs must be Index"
with pytest.raises(TypeError, match=msg):
    ci.append(ci.values.set_categories(list("abcd")))
with pytest.raises(TypeError, match=msg):
    ci.append(ci.values.reorder_categories(list("abc")))
