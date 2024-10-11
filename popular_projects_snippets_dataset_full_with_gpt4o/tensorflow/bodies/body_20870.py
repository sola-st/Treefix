# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
for dtype, use_gpu in itertools.product(
    [np.float16, np.float32, np.float64], [False, True]):
    var = np.arange(100).astype(dtype)
    m = np.arange(1, 101).astype(dtype)
    v = np.arange(101, 201).astype(dtype)
    grad = np.arange(100).astype(dtype)
    self._testTypesForAdam(var, m, v, grad, use_gpu)
