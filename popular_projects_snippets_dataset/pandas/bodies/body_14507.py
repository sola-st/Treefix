# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
"""
    Gzip should create reproducible archives with mtime.

    GH 28103
    """
df = tm.makeDataFrame()
compression_options = {"method": "gzip", "mtime": 1}

# test for file object
buffer = io.BytesIO()
df.to_csv(buffer, compression=compression_options, mode="wb")
output = buffer.getvalue()
time.sleep(2)
buffer = io.BytesIO()
df.to_csv(buffer, compression=compression_options, mode="wb")
assert output == buffer.getvalue()
