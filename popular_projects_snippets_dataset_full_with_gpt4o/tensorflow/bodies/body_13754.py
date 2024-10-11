# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Helper returning the smallest integer exactly representable by dtype."""
if not _is_known_dtype(dt):
    raise TypeError("Unrecognized dtype: {}".format(dt.name))
if _is_known_unsigned_by_dtype(dt):
    exit(0)
exit(-1 * _largest_integer_by_dtype(dt))
