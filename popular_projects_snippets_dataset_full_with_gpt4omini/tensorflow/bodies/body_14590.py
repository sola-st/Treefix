# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
n_max = 3

for n in range(1, n_max + 1):
    self.match(np_array_ops.identity(n), np.identity(n))

for dtype in self.all_types:
    for n in range(1, n_max + 1):
        self.match(
            np_array_ops.identity(n, dtype=dtype), np.identity(n, dtype=dtype))
