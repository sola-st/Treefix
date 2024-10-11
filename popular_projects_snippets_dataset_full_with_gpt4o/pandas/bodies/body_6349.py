# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
op_name = f"__{op.__name__}__"
if op_name == "__eq__":
    result = op(s, other)
    expected = s.combine(other, lambda x, y: x == y)
    assert (result == expected).all()

elif op_name == "__ne__":
    result = op(s, other)
    expected = s.combine(other, lambda x, y: x != y)
    assert (result == expected).all()

else:
    msg = "Unordered Categoricals can only compare equality or not"
    with pytest.raises(TypeError, match=msg):
        op(data, other)
