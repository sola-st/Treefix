# Extracted from ./data/repos/pandas/pandas/tests/frame/test_logical_ops.py
# GH#5808

df1 = DataFrame(1.0, index=[1], columns=["A"])
df2 = DataFrame(True, index=[1], columns=["A"])
msg = re.escape("unsupported operand type(s) for |: 'float' and 'bool'")
with pytest.raises(TypeError, match=msg):
    df1 | df2

df1 = DataFrame("foo", index=[1], columns=["A"])
df2 = DataFrame(True, index=[1], columns=["A"])
msg = re.escape("unsupported operand type(s) for |: 'str' and 'bool'")
with pytest.raises(TypeError, match=msg):
    df1 | df2
