# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
index = tm.makeStringIndex(100)

msg = "unsupported operand type|Cannot broadcast"
with pytest.raises(TypeError, match=msg):
    index - "a"
with pytest.raises(TypeError, match=msg):
    index - index
with pytest.raises(TypeError, match=msg):
    index - index.tolist()
with pytest.raises(TypeError, match=msg):
    index.tolist() - index
