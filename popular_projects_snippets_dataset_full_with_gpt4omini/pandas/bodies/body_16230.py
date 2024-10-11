# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
s_1111 = Series([1] * 4, dtype="int8")
msg = "Cannot perform 'and_' with a dtyped.+array and scalar of type"
with pytest.raises(TypeError, match=msg):
    s_1111 & "a"
with pytest.raises(TypeError, match="unsupported operand.+for &"):
    s_1111 & ["a", "b", "c", "d"]
