# Extracted from ./data/repos/pandas/pandas/tests/frame/test_unary.py
msg = r"bad operand type for unary \+: 'DatetimeArray'"
with pytest.raises(TypeError, match=msg):
    (+df)
with pytest.raises(TypeError, match=msg):
    (+df["a"])
