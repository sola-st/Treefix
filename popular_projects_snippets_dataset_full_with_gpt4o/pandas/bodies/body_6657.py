# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_constructors.py
msg = f"Value needs to be a scalar value, was type {type(args).__name__}"
with pytest.raises(TypeError, match=msg):
    RangeIndex(args)
