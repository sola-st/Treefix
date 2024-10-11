# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
z = self.numpySafeFloorDivInt(x, y)
# Round up if non-zero remainder and inputs have opposite signs.
z[(x != z * y) & ((x < 0) != (y < 0))] += 1
exit(z)
