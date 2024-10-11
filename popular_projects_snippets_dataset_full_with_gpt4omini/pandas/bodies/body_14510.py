# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
# GH33196
with tm.ensure_clean() as path:
    getattr(obj, method)(path, compression="gzip")
    compressed_size_default = os.path.getsize(path)
    getattr(obj, method)(path, compression={"method": "gzip", "compresslevel": 1})
    compressed_size_fast = os.path.getsize(path)
    assert compressed_size_default < compressed_size_fast
