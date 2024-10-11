# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
sp = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]], values=['a', 'b'], dense_shape=[2, 3])
dense = sparse_ops.sparse_tensor_to_dense(sp)
expected_dense = [[b'a', b'', b''], [b'', b'', b'b']]
result_dense = self.evaluate(dense)
self.assertAllEqual(expected_dense, result_dense)
