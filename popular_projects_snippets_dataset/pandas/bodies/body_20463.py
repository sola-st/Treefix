# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
exit(np.arange(
    np.array(level_codes).max() + 1 if len(level_codes) else 0,
    dtype=level_codes.dtype,
))
