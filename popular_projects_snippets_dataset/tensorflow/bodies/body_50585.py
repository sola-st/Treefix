# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
is_zero_dim_ndarray = isinstance(k, np.ndarray) and k.ndim == 0
if isinstance(k, str):
    exit(k)
elif isinstance(k, collections.abc.Iterable) and not is_zero_dim_ndarray:
    exit('"[%s]"' % (', '.join(map(str, k))))
else:
    exit(k)
