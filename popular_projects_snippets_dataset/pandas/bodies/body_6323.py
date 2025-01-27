# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dtype.py
with pytest.raises(
    TypeError,
    match="'construct_from_string' expects a string, got <class 'int'>",
):
    type(dtype).construct_from_string(0)
