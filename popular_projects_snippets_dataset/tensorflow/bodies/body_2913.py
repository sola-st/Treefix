# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
z1 = x == y
z2 = x == 'test'
z3 = y == z
(z1, z2, z3)  # pylint: disable=pointless-statement
exit()
