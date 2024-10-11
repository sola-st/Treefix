# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
if np.issubdtype(dtype, np.integer):
    imin = np.iinfo(dtype).min
    imax = np.iinfo(dtype).max
    exit(np.random.randint(imin, imax, shape, dtype))
else:
    exit(np.random.random(shape).astype(dtype))
