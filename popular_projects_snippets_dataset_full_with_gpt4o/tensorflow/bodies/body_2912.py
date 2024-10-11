# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
# int
z0 = [x, y]
z1 = x == y
z2 = x < y
z3 = x <= y
z4 = x > y
z5 = x >= y
z6 = x != y
z7 = x + y
z8 = x - y
z8 += x
z8 += 1
(z0, z1, z2, z3, z4, z5, z6, z7, z8)  # pylint: disable=pointless-statement

# float
z9 = x1 > y1
z10 = x1 + y1
z11 = [x1, y1]
(z9, z10, z11)  # pylint: disable=pointless-statement
exit()
