# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
cat = Categorical(["a", "b", "a"])
message = re.escape("removals must all be in old categories: {'c'}")

with pytest.raises(ValueError, match=message):
    cat.remove_categories(removals)
