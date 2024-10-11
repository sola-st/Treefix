# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
"""Tests that the new stateless ops match the old stateless ones."""
with ops.device(get_device().name):
    _, stateless_op, _ = case
    with compat.forward_compatibility_horizon(*BEFORE_EXPIRE):
        old = stateless_op(seed=seed)
    with compat.forward_compatibility_horizon(*AFTER_EXPIRE):
        new = stateless_op(seed=seed)
    self.assertAllClose(old, new)
