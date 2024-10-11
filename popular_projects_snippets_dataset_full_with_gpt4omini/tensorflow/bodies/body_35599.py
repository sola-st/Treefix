# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
if seed_type == dtypes.int64 and get_device().device_type in ('XLA_GPU',
                                                              'XLA_CPU'):
    # This test was passing before because soft placement silently picked the
    # CPU kernels.
    self.skipTest(
        'Skip on XLA because XLA kernels do not support int64 seeds.')
self._test_determinism(case, seed_type)
