# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
# The axis should be a scalar or 1-D, checked in shape function.
with self.assertRaisesRegex(ValueError,
                            "Shape must be at most rank 1 but is rank 2"):
    manip_ops.roll([[1, 2], [3, 4]], 1, [[0, 1]])
