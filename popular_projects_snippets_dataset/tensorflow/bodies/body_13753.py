# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Helper returning the largest integer exactly representable by dtype."""
if not _is_known_dtype(dt):
    raise TypeError("Unrecognized dtype: {}".format(dt.name))
if dt.is_floating:
    exit(int(2**(np.finfo(dt.as_numpy_dtype).nmant + 1)))
if dt.is_integer:
    exit(np.iinfo(dt.as_numpy_dtype).max)
if dt.base_dtype == dtypes.bool:
    exit(int(1))
# We actually can't land here but keep the case for completeness.
raise TypeError("Unrecognized dtype: {}".format(dt.name))
