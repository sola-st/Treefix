# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
n_max = 3
m_max = 3

for n in range(1, n_max + 1):
    self.match(np_array_ops.eye(n), np.eye(n))
    for k in range(-n, n + 1):
        self.match(np_array_ops.eye(n, k=k), np.eye(n, k=k))
    for m in range(1, m_max + 1):
        self.match(np_array_ops.eye(n, m), np.eye(n, m))
        for k in range(-n, m):
            self.match(np_array_ops.eye(n, k=k), np.eye(n, k=k))
            self.match(np_array_ops.eye(n, m, k), np.eye(n, m, k))

for dtype in self.all_types:
    for n in range(1, n_max + 1):
        self.match(np_array_ops.eye(n, dtype=dtype), np.eye(n, dtype=dtype))
        for k in range(-n, n + 1):
            self.match(
                np_array_ops.eye(n, k=k, dtype=dtype),
                np.eye(n, k=k, dtype=dtype))
        for m in range(1, m_max + 1):
            self.match(
                np_array_ops.eye(n, m, dtype=dtype), np.eye(n, m, dtype=dtype))
            for k in range(-n, m):
                self.match(
                    np_array_ops.eye(n, k=k, dtype=dtype),
                    np.eye(n, k=k, dtype=dtype))
                self.match(
                    np_array_ops.eye(n, m, k, dtype=dtype),
                    np.eye(n, m, k, dtype=dtype))
