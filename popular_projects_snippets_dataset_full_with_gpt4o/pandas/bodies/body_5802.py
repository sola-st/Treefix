# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# GH 50667
pa_type = data.dtype.pyarrow_dtype
if pa.types.is_integer(pa_type):
    assert is_integer_dtype(data)
else:
    assert not is_integer_dtype(data)
