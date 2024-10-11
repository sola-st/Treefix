# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
cat = Categorical(["a", "b", "c", "b"], ordered=False)
msg = (
    f"Categorical is not ordered for operation {method}\n"
    "you can use .as_ordered() to change the Categorical to an ordered one"
)
method = getattr(np, method)
with pytest.raises(TypeError, match=re.escape(msg)):
    method(cat)
