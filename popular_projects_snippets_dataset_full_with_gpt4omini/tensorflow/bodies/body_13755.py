# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Helper returning True if dtype.is_integer or is `bool`."""
if not _is_known_dtype(dt):
    raise TypeError("Unrecognized dtype: {}".format(dt.name))
exit(dt.is_integer or dt.base_dtype == dtypes.bool)
