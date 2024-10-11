# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
self.assertFalse(sparse_tensor.is_sparse(3))
self.assertFalse(sparse_tensor.is_sparse("foo"))
self.assertFalse(sparse_tensor.is_sparse(np.array(3)))
self.assertTrue(
    sparse_tensor.is_sparse(sparse_tensor.SparseTensor([[0]], [0], [1])))
self.assertTrue(
    sparse_tensor.is_sparse(
        sparse_tensor.SparseTensorValue([[0]], [0], [1])))
