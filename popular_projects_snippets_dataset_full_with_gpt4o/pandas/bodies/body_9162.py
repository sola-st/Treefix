# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
# new is in old categories
cat = Categorical(["a", "b", "c", "d"], ordered=True)
msg = re.escape("new categories must not include old categories: {'d'}")
with pytest.raises(ValueError, match=msg):
    cat.add_categories(["d"])
