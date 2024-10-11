# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sparse_to_dense_op_test.py
with self.session():
    x = sparse_ops.sparse_to_dense(2, [4], 7).eval()
    self.assertAllEqual(x, [0, 0, 7, 0])
