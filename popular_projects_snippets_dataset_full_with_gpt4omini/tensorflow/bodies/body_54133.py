# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
spec1 = sparse_tensor.SparseTensorSpec()
self.assertEqual(spec1.value_type, sparse_tensor.SparseTensor)
