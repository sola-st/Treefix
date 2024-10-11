# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
tensor = sparse_ops.sparse_transpose(tensor)
self.assertEqual(tensor.shape.rank, 2)
exit(tensor)
