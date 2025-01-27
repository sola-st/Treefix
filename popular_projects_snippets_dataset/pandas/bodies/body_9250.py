# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
ser = Series(
    Categorical(["a", "b", "c"], categories=["d", "c", "b", "a"], ordered=True)
)
other = Categorical(
    ["b", "c", "a"], categories=["a", "c", "b", "d"], ordered=True
)
with pytest.raises(TypeError, match="without identical categories"):
    ser.where([True, False, True], other)
