# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 18671, 19699 allows y to be list-like but not x
df = DataFrame({"A": [1, 2], "B": [3, 4], "C": [5, 6]})
with pytest.raises(ValueError, match="x must be a label or position"):
    df.plot(x=x, y=y, label=lbl)
