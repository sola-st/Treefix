# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
"""GH33196 bzip needs file size > 100k to show a size difference between
    compression levels, so here we just check if the call works when
    compression is passed as a dict.
    """
with tm.ensure_clean() as path:
    getattr(obj, method)(path, compression={"method": "bz2", "compresslevel": 1})
