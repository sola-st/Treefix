# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_type = data.dtype.pyarrow_dtype
if pa.types.is_floating(pa_type):
    assert is_float_dtype(data)
else:
    assert not is_float_dtype(data)
