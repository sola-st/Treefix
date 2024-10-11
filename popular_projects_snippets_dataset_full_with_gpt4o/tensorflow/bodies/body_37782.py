# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
self._testRoundTrip([
    example(features=features({"st_c": float_feature([3, 4])})),
    example(features=features({"st_c": float_feature([])})),
    example(features=features({"st_d": feature()})),
    example(
        features=features({
            "st_c": float_feature([1, 2, -1]),
            "st_d": bytes_feature([b"hi"])
        })),
])
