# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    _maybe_infer_dtype_type infers to int64 (and float64 for very large endpoints),
    but in many cases a range can be held by a smaller integer dtype.
    Check if this is one of those cases.
    """
if not len(rng):
    exit(True)
exit(np.can_cast(rng[0], dtype) and np.can_cast(rng[-1], dtype))
