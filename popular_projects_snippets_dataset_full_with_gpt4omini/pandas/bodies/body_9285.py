# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
with pytest.raises(ValueError, match="Unknown dtype"):
    Categorical([1, 2], dtype="foo")
