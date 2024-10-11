# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
msg = "Both were None"
with pytest.raises(ValueError, match=msg):
    Categorical.from_codes([0, 1])
