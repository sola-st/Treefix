# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_constructors.py
msg = f"Wrong type {type(args)} for value {args}"
with pytest.raises(TypeError, match=msg):
    RangeIndex(args)
