# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
if get_device().device_type != 'GPU':
    # This test compares the numbers produced by the CPU and GPU kernel for
    # stateless_random_gamma.
    self.skipTest('This test requires GPU')
self._test_match_stateless_cpu_gpu(case, seed)
