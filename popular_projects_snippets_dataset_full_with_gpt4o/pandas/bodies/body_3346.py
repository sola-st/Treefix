# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH 21977
ser = Series([["a", "b"], [], np.nan, [1]])
obj = DataFrame({"col": ser})
obj = tm.get_obj(obj, frame_or_series)
expected = obj
result = obj.replace([], np.nan)
tm.assert_equal(result, expected)

# GH 19266
msg = (
    "NumPy boolean array indexing assignment cannot assign {size} "
    "input values to the 1 output values where the mask is true"
)
with pytest.raises(ValueError, match=msg.format(size=0)):
    obj.replace({np.nan: []})
with pytest.raises(ValueError, match=msg.format(size=2)):
    obj.replace({np.nan: ["dummy", "alt"]})
