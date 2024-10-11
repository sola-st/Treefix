# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dtype.py
msg = f"Cannot construct a '{type(dtype).__name__}' from 'another_type'"
with pytest.raises(TypeError, match=msg):
    type(dtype).construct_from_string("another_type")
