# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
msg = r"'another_type' must end with '\[pyarrow\]'"
with pytest.raises(TypeError, match=msg):
    type(dtype).construct_from_string("another_type")
