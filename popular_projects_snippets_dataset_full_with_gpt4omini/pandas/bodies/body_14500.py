# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
if compression_only == "tar":
    compression_only = {"method": "tar", "mode": "w:gz"}

with tm.ensure_clean() as path:
    getattr(obj, method)(path, compression=compression_only)
    compressed_size = os.path.getsize(path)
    getattr(obj, method)(path, compression=None)
    uncompressed_size = os.path.getsize(path)
    assert uncompressed_size > compressed_size
