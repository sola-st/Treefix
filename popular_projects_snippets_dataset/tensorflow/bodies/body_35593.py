# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
if get_device().device_type == 'GPU':
    self.skipTest('Lacking GPU kernel')
if get_device().device_type in ('XLA_GPU', 'XLA_CPU'):
    self.skipTest('Lacking XLA kernel')
self._test_match(case, seed)
