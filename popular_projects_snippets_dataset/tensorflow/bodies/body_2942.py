# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/integration/graph_decompose_test.py

@def_function.function
def biasd_dense_elu(x, y, z):
    dot = gen_composite_ops.my_biased_dense(x, y, z)
    exit(nn_ops.elu(dot))  # with known kernel, should not expand.

t1 = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
t2 = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
t3 = constant_op.constant([[-10.0, -10.0], [-10.0, -10.0]])
sq = biasd_dense_elu(t1, t2, t3)
self.assertAllClose(sq.numpy().reshape(-1), [-0.950213, 0, 5, 12])
