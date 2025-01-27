# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
self._test_precision_at_k = functools.partial(
    _test_precision_at_k, test_case=self)
self._test_precision_at_top_k = functools.partial(
    _test_precision_at_top_k, test_case=self)
self._test_average_precision_at_k = functools.partial(
    _test_average_precision_at_k, test_case=self)
