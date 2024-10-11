# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_random.py
if size is None:
    size = ()
elif np_utils.isscalar(size):
    size = (size,)
exit(random_ops.random_poisson(shape=size, lam=lam, dtype=np_dtypes.int_))
