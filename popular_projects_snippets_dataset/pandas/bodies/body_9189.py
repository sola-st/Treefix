# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
cat = Categorical(["a", "b", "c", "b"], ordered=True)
method = getattr(np, method)
result = method(cat, axis=None)
assert result == expected
