# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
self._testRoundTrip([
    example(features=features({"a": float_feature([1, 1, 3])})),
    example(features=features({"a": float_feature([-1, -1, 2])})),
])
