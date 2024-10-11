# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
"""
    Gzip should create reproducible archives with mtime.

    Note: Archives created with different filenames will still be different!

    GH 28103
    """
df = tm.makeDataFrame()
compression_options = {"method": "gzip", "mtime": 1}

# test for filename
with tm.ensure_clean() as path:
    path = Path(path)
    df.to_csv(path, compression=compression_options)
    time.sleep(2)
    output = path.read_bytes()
    df.to_csv(path, compression=compression_options)
    assert output == path.read_bytes()
