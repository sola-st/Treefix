# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
with context.graph_mode():
    sp = sparse_tensor.SparseTensor([[0, 0], [1, 2]], [1.0, 3.0], [3, 4])
    w = ops.convert_to_tensor(np.ones([4, 1], np.float32))
    out = sparse_ops.sparse_tensor_dense_matmul(sp, w)
    self.assertEqual(len(sp.consumers()), 1)
    self.assertEqual(sp.consumers()[0], out.op)

    dense = sparse_ops.sparse_tensor_to_dense(sp)
    self.assertEqual(len(sp.consumers()), 2)
    self.assertIn(dense.op, sp.consumers())
    self.assertIn(out.op, sp.consumers())
