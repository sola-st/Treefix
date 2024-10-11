# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
self._run_test(self._rng.randn(2, 2, int(3*4/2)),
               use_deferred_shape=True,
               upper=True)
