# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
for (dtype, use_gpu) in itertools.product(
    [np.float16, np.float32, np.float64], [False, True]):
    x = np.arange(100).astype(dtype)
    alpha = np.array(2.0).astype(dtype)
    delta = np.arange(100).astype(dtype)
    self._testTypes(x, alpha, delta, use_gpu)
