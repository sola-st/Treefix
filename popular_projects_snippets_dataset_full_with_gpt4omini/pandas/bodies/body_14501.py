# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
with tm.ensure_clean() as path:
    with icom.get_handle(
        path,
        "w:gz" if compression_only == "tar" else "w",
        compression=compression_only,
    ) as handles:
        getattr(obj, method)(handles.handle)
        assert not handles.handle.closed
    compressed_size = os.path.getsize(path)
with tm.ensure_clean() as path:
    with icom.get_handle(path, "w", compression=None) as handles:
        getattr(obj, method)(handles.handle)
        assert not handles.handle.closed
    uncompressed_size = os.path.getsize(path)
    assert uncompressed_size > compressed_size
