# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
self.check(
    array_ops.fill, (2, 3),
    'dims must be a vector', [3, 3],
    lenient=[5, 6],
    strict=[])
self.check(
    array_ops.fill, ([2], [3]),
    'value must be a scalar', [3, 3],
    lenient=[5, 6],
    strict=[])
