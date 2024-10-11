# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
z = array_ops.Split(axis=0, value=x, num_split=2)
exit((z[0], z[1]))
