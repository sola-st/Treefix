# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
# The input should be 1-D or higher, checked in shape function.
with self.assertRaisesRegex(ValueError,
                            "Shape must be at least rank 1 but is rank 0"):
    manip_ops.roll(7, 1, 0)
