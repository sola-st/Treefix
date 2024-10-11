# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
spec1 = sparse_tensor.SparseTensorSpec()
self.assertEqual(spec1.shape.rank, None)
self.assertEqual(spec1.dtype, dtypes.float32)

spec2 = sparse_tensor.SparseTensorSpec([None, None], dtypes.string)
self.assertEqual(spec2.shape.as_list(), [None, None])
self.assertEqual(spec2.dtype, dtypes.string)
