# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# GH#9016: support bitwise op for integer types
s_0123 = Series(range(4), dtype="int64")

msg = "Cannot perform.+with a dtyped.+array and scalar of type"
with pytest.raises(TypeError, match=msg):
    s_0123 & np.NaN
with pytest.raises(TypeError, match=msg):
    s_0123 & 3.14
msg = "unsupported operand type.+for &:"
with pytest.raises(TypeError, match=msg):
    s_0123 & [0.1, 4, 3.14, 2]
with pytest.raises(TypeError, match=msg):
    s_0123 & np.array([0.1, 4, 3.14, 2])
with pytest.raises(TypeError, match=msg):
    s_0123 & Series([0.1, 4, -3.14, 2])
