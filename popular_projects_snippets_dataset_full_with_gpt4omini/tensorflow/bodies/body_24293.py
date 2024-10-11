# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
"""Test running multiple steps of eager execution without Inf/NaN."""
check_numerics_callback.enable_check_numerics()
x = constant_op.constant([2.0, 3.0])
y = constant_op.constant([1.0, 0.0])
self.assertAllClose((x + y) * (x - y), [3.0, 9.0])
