# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    matmul = def_function.function(math_ops.matmul)
    t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
    sq = matmul(t, t, transpose_a=True)
    self.assertAllEqual(sq.numpy().reshape(-1), [10, 14, 14, 20])
