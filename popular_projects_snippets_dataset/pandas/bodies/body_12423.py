# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
with pytest.raises(UnsupportedOperation, match="fileno"):
    with BytesIO() as buffer:
        icom.get_handle(buffer, "rb", memory_map=True)
