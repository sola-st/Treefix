# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH#38433
with pytest.raises(TypeError, match="Categorical input must be list-like"):
    Categorical("A", categories=["A", "B"])
