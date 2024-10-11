# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
z, _ = array_ops.Split(axis=0, value=x, num_split=2)
(y, pred)  # pylint: disable=pointless-statement
exit(z)
