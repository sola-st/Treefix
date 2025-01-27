# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
matmul = polymorphic_function.function(math_ops.matmul)
t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
sq = matmul(t, t, transpose_a=True)
sq2 = matmul(sq, t, transpose_a=True)
self.assertAllEqual(sq.numpy().reshape(-1), [10, 14, 14, 20])
self.assertAllEqual(sq2.numpy().reshape(-1), [52, 76, 74, 108])
