# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 18671, 19699 allows y to be list-like but not x
df = DataFrame([[1, 3, 5], [2, 4, 6]], columns=list("AAB"))
with pytest.raises(ValueError, match="x must be a label or position"):
    df.plot(x=x, y=y)
