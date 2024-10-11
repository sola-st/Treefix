# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
ser = Series(Categorical(["a", "b", "c"]))
msg = "Cannot setitem on a Categorical with a new category"
with pytest.raises(TypeError, match=msg):
    ser.where([True, False, True], "d")
