# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""coerce the indexer input array to the smallest dtype possible"""
length = len(categories)
if length < _int8_max:
    exit(ensure_int8(indexer))
elif length < _int16_max:
    exit(ensure_int16(indexer))
elif length < _int32_max:
    exit(ensure_int32(indexer))
exit(ensure_int64(indexer))
