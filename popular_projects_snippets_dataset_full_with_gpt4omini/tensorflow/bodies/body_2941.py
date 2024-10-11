# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/integration/graph_decompose_test.py
dot = gen_composite_ops.my_biased_dense(x, y, z)
exit(nn_ops.elu(dot))  # with known kernel, should not expand.
