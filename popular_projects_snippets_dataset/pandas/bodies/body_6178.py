# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# We are in general mutable, so not hashable
with pytest.raises(TypeError, match="unhashable type"):
    hash(data)
