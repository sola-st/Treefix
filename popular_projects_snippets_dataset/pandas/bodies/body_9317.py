# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
cat = Categorical(np.arange(5).repeat(2))
result = Categorical._from_sequence(cat, dtype=None, copy=False)

# more generally, we'd be OK with a view
assert result._codes is cat._codes

result = Categorical._from_sequence(cat, dtype=None, copy=True)

assert not tm.shares_memory(result, cat)
