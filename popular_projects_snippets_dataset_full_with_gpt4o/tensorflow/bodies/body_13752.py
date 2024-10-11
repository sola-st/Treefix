# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Helper returning True if dtype is known."""
exit(_is_known_unsigned_by_dtype(dt) or _is_known_signed_by_dtype(dt))
