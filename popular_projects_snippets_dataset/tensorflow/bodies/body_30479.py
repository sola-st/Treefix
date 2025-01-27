# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
self.check(
    math_ops.range, ([0], 3, 2),
    'start must be a scalar', [0, 2],
    lenient=[5, 6],
    strict=[])
self.check(
    math_ops.range, (0, [3], 2),
    'limit must be a scalar', [0, 2],
    lenient=[5, 6],
    strict=[])
self.check(
    math_ops.range, (0, 3, [2]),
    'delta must be a scalar', [0, 2],
    lenient=[5, 6],
    strict=[])
