# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
"""Tests that alg=philox and alg=None are the same (on CPU/GPU)."""
with ops.device(get_device().name):
    _, stateless_op, _ = case
    implicit_alg = stateless_op(seed=seed)
    # All device types allowed in this test will result in Philox
    explicit_alg = stateless_op(seed=seed, alg='philox')
    self.assertAllClose(implicit_alg, explicit_alg)
