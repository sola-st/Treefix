# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/integration/graph_decompose_test.py
biased_dense = def_function.function(gen_composite_ops.my_biased_dense)
t1 = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
t2 = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
t3 = constant_op.constant([[-10.0, -10.0], [-10.0, -10.0]])
sq = biased_dense(t1, t2, t3, act='relu')
self.assertAllEqual(sq.numpy().reshape(-1), [0, 0, 5, 12])
