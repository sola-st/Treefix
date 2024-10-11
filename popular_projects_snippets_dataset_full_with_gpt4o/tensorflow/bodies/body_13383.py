# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
with ops.Graph().as_default():
    t = sparse_tensor.SparseTensor(indices=[[0, 0]],
                                   values=[0.],
                                   dense_shape=[3, 4])
    self.assertTrue(t.shape.is_fully_defined)
    transposed = sparse_ops.sparse_transpose(t)
    self.assertAllEqual(transposed.shape, [4, 3])
