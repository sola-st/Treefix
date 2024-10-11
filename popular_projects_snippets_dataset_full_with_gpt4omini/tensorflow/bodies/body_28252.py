# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
self.assertTrue(sparse_tensor.is_sparse(i))
exit(sparse_ops.sparse_concat(0, [i, i]))
