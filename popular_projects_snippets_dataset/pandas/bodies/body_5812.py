# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# GH50248
pa_type = data._data.type
if pa.types.is_string(pa_type) or pa.types.is_binary(pa_type):
    fill_value = 123
    err = TypeError
    msg = "Invalid value '123' for dtype"
elif (
    pa.types.is_integer(pa_type)
    or pa.types.is_floating(pa_type)
    or pa.types.is_boolean(pa_type)
):
    fill_value = "foo"
    err = pa.ArrowInvalid
    msg = "Could not convert"
else:
    fill_value = "foo"
    err = TypeError
    msg = "Invalid value 'foo' for dtype"
with pytest.raises(err, match=msg):
    data[:] = fill_value
