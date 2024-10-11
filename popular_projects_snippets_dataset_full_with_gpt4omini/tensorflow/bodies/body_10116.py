# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
# Numpy crashes with a FPE for INT_MIN % -1.
z = self.numpySafeFloorDivInt(x, y)
exit(x - z * y)
