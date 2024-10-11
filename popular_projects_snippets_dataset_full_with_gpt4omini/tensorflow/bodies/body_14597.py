# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for a, dtype in itertools.product(self.all_arrays, self.all_types):
    self.match(
        np_array_ops.ascontiguousarray(a, dtype=dtype),
        np.ascontiguousarray(a, dtype=dtype))
