# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
cat = Categorical(["a", "b", "c", "a"], ordered=True)
msg = "items in new_categories are not the same as in old categories"
with pytest.raises(ValueError, match=msg):
    cat.reorder_categories(new_categories)
