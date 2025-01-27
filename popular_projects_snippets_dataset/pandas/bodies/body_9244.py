# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
cat = Categorical(["a", "b", "c", "a"])
msg = (
    "new categories need to have the same number of items "
    "as the old categories!"
)
with pytest.raises(ValueError, match=msg):
    cat.rename_categories(new_categories)
