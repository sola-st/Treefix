# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 47215
data = [[1, 2, 3], [4, 5, 6]]
with pytest.raises(ValueError, match="index cannot be a set"):
    DataFrame(data, index={"a", "b"})
with pytest.raises(ValueError, match="columns cannot be a set"):
    DataFrame(data, columns={"a", "b", "c"})
