# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
df = DataFrame([0])
msg = r"unsupported operand type\(s\) for \+: 'int' and 'str'"
with pytest.raises(TypeError, match=msg):
    df.groupby(lambda x: x + "foo")
