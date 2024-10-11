# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
# The shift and axis must be same size, checked in shape function.
with self.assertRaisesRegex(ValueError, "both shapes must be equal"):
    manip_ops.roll([[1, 2], [3, 4]], [1], [0, 1])
