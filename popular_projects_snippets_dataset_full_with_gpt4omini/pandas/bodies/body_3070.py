# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_axis.py
# wrong values for the "axis" parameter
with pytest.raises(ValueError, match="No axis named"):
    obj.set_axis(list("abc"), axis=axis)
