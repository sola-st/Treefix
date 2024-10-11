# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
m = map_ops.empty_tensor_map()
s = map_ops.tensor_map_size(m)
self.assertAllEqual(s, 0)
