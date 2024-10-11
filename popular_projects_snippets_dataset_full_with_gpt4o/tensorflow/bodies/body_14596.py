# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for a, dtype in itertools.product(self.all_arrays, self.all_types):
    self.match(
        np_array_ops.asanyarray(a, dtype=dtype),
        np.asanyarray(a, dtype=dtype))
zeros_list = np_array_ops.zeros(5)
# Same instance is returned if no dtype is specified and input is ndarray.
self.assertIs(np_array_ops.asanyarray(zeros_list), zeros_list)
with ops.device('CPU:1'):
    self.assertIs(np_array_ops.asanyarray(zeros_list), zeros_list)
# Different instance is returned if dtype is specified and input is ndarray.
self.assertIsNot(np_array_ops.asanyarray(zeros_list, dtype=int), zeros_list)
