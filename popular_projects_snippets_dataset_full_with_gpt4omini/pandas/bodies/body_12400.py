# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
with StringIO() as input_buffer:
    with icom.get_handle(input_buffer, "r") as handles:
        assert handles.handle == input_buffer
    assert not input_buffer.closed
assert input_buffer.closed
