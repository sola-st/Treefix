# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_type = data.dtype.pyarrow_dtype
if pa.types.is_signed_integer(pa_type):
    assert is_signed_integer_dtype(data)
else:
    assert not is_signed_integer_dtype(data)
