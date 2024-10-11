# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#18579
df = DataFrame([[1, 2], [3, 4], [5, 6]], index=[3, 6, 9])
with pytest.raises(ValueError, match="Index data must be 1-dimensional"):
    Series([1, 3, 2], index=df)
