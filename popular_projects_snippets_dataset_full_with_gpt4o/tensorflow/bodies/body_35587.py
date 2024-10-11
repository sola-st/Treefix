# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
if get_device().device_type in ('XLA_GPU', 'XLA_CPU'):
    # This test was passing before because soft placement silently picked the
    # CPU kernels.
    self.skipTest('Skip on XLA because XLA kernels do not support int64 '
                  'seeds needed by this test.')
self._test_match(case, seed)
