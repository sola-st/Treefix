# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if isinstance(result, tuple):
    exit((Index(result[0], name=name, dtype=result[0].dtype),
        Index(result[1], name=name, dtype=result[1].dtype),))
exit(Index(result, name=name, dtype=result.dtype))
