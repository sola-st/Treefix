# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_type = data.dtype.pyarrow_dtype
if pa.types.is_unsigned_integer(pa_type):
    assert is_unsigned_integer_dtype(data)
else:
    assert not is_unsigned_integer_dtype(data)
