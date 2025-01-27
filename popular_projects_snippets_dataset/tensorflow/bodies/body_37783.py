# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
aname = "a"
bname = "b*has+a:tricky_name"
self._testRoundTrip([
    example(
        features=features({
            aname: float_feature([1, 1]),
            bname: bytes_feature([b"b0_str"])
        })),
    example(
        features=features({
            aname: float_feature([-1, -1]),
            bname: bytes_feature([b"b1"])
        })),
])
