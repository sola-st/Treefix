# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
with pytest.raises(ValueError, match="Categorical categories must be unique"):
    Categorical.from_codes([0, 1, 2], categories=["a", "a", "b"])
