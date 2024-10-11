# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# GH 50563
pa_type = data.dtype.pyarrow_dtype
if (
    pa.types.is_floating(pa_type)
    or pa.types.is_integer(pa_type)
    or pa.types.is_decimal(pa_type)
):
    assert is_numeric_dtype(data)
else:
    assert not is_numeric_dtype(data)
