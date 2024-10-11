# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
cat = Categorical(["a", "b", "c", "a"], ordered=True)
cat2 = cat.as_unordered()
assert not cat2.ordered
cat2 = cat.as_ordered()
assert cat2.ordered

assert cat2.set_ordered(True).ordered
assert not cat2.set_ordered(False).ordered

# removed in 0.19.0
msg = (
    "property 'ordered' of 'Categorical' object has no setter"
    if PY311
    else "can't set attribute"
)
with pytest.raises(AttributeError, match=msg):
    cat.ordered = True
with pytest.raises(AttributeError, match=msg):
    cat.ordered = False
